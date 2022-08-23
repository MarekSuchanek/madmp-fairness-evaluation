# maDMP FAIRness Evaluation Example

*Example evaluator of FAIRness for maDMPs according to [RDA DMP Common Standard](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard)*

## Motivation and Objectives

This machine-actionable DMP evaluator prototype serves to check FAIRness of the datasets mentioned in maDMP created according to the [RDA DMP Common Standard](https://github.com/RDA-DMP-Common/RDA-DMP-Common-Standard) in JSON format. You can provide any such DMP as an input for the evaluator (you can also use the provided [examples](./examples/)). The evaluator will extract every dataset identifier (JSON path `dmp/dataset/dataset_id/identifier`) and check its FAIRness via calling [F-UJI](https://github.com/pangaea-data-publisher/fuji) API. As a result, overall FAIR score (percentage) and information about passed/failed tests is presented for each dataset in the DMP. The goal is to allow quick check of achieved FAIRness in a DMP for both authors and funders.

## Requirements

* You need F-UJI API running (you can use [`docker-compose.yml`](docker-compose.yml)), 
  visit [pangaea-data-publisher/fuji](https://github.com/pangaea-data-publisher/fuji) repository for more information.
* Python 3.6+ (preferably used with [virtualenv](https://docs.python.org/3/library/venv.html))

## Usage

### Install dependencies

```
python3 -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

Alternatively, on Windows:

```
python -m venv env
env\Scripts\activate.bat
python -m pip install -r requirements.txt
```

### Get help

```shell
python madmp-evaluate-fairness.py --help
```

### Evaluate

```shell
python madmp-evaluate-fairness.py examples/ex6-dmp-passing.json
```

Example output:

```
https://doi.org/10.1594/PANGAEA.908011 - FAIR score: 91.67%
  FsF-F1-01D: pass
  FsF-F1-02D: pass
  FsF-F2-01M: pass
  FsF-F3-01M: pass
  FsF-F4-01M: pass
  FsF-A1-01M: pass
  FsF-I1-01M: pass
  FsF-I2-01M: pass
  FsF-I3-01M: pass
  FsF-R1-01MD: pass
  FsF-R1.1-01M: pass
  FsF-R1.2-01M: pass
  FsF-R1.3-01M: pass
  FsF-R1.3-02D: pass
  FsF-A1-03D: pass
  FsF-A1-02M: pass
```

If needed, you can specify F-UJI endpoint and credentials, see `--help`.

## License

This project is licensed under the Apache License v2.0 - see the
[LICENSE](LICENSE) file for more details.
