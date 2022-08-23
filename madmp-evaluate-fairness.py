import click
import json
import requests

FUJI_ENDPOINT = 'http://127.0.0.1:1071/fuji/api/v1/evaluate'
FUJI_USERNAME = 'marvel'
FUJI_PASSWORD = 'wonderwoman'


def extract_dataset(madmp_json):
    dmp = madmp_json['dmp']
    datasets = dmp['dataset']
    dataset_uris = [
        dataset['dataset_id']['identifier']
        for dataset in datasets
    ]
    return dataset_uris


def fuji_evaluate(dataset_uri, endpoint, username, password):
    payload = {
        'metadata_service_endpoint': 'http://ws.pangaea.de/oai/provider',
        'metadata_service_type': 'oai_pmh',
        'object_identifier': dataset_uri,
        'test_debug': True,
        'use_datacite': True
    }
    res = requests.post(
        url=endpoint,
        json=payload,
        auth=(username, password),
    )
    res.raise_for_status()
    return res.json()


@click.command()
@click.argument('madmp', type=click.File(mode='r'))
@click.option('--fuji', type=str, default=FUJI_ENDPOINT,
              help='Evaluation endpoint of F-UJI.')
@click.option('--fuji-username', type=str, default=FUJI_USERNAME,
              help='F-UJI API username.')
@click.option('--fuji-password', type=str, default=FUJI_PASSWORD,
              help='F-UJI API password.')
def cli(madmp, fuji, fuji_username, fuji_password):
    dataset_uris = []
    try:
        madmp_json = json.load(madmp)
        dataset_uris = extract_dataset(madmp_json)
    except KeyError as e:
        click.echo(f'Invalid maDMP in JSON: {str(e)}', err=True)
    except Exception as e:
        click.echo(f'Cannot parse JSON: {str(e)}', err=True)
    for dataset_uri in dataset_uris:
        try:
            report = fuji_evaluate(dataset_uri, fuji, fuji_username, fuji_password)
            percent = click.style(f'{report["summary"]["score_percent"]["FAIR"]}%', bold=True)
            click.echo(f'{dataset_uri} - FAIR score: {percent}%')
            for result in report['results']:
                status = click.style('fail', fg='red', bold=True)
                if result['test_status'] == 'pass':
                    status = click.style('pass', fg='green', bold=True)
                click.echo(f'  {result["metric_identifier"]}: {status}')
        except Exception as e:
            click.echo(f'{dataset_uri} - failed: {str(e)}')
        click.echo('-'*50)


if __name__ == '__main__':
    cli()
