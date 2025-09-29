# DatabricksDABs
Test deployment of databricks using DABs


databricks auth login --host https://adb-3409237260072496.16.azuredatabricks.net

Deploy the bundle : databricks bundle deploy -t dev

Run a job or notebook : databricks bundle run sample_notebook.py -t dev




databricks bundle validate
databricks bundle deploy -t dev
databricks bundle run -t dev hello_job



Check databricks.yml configuration settings
https://docs.databricks.com/aws/en/dev-tools/bundles/settings