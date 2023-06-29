# ReportLab Flowable for RML Template

This example shows how to create and use a ReportLab Flowable for use with ReportLab's RML templating language. The RML `<plugInFlowable />` element

All the examples I could find show how to do this programmatically, but do not work with the RML templating language.

## Install and Run
The Poetry project uses Python 3.11, but there's nothing 3.11-specific about the code.

You will need access to the ReportLab commercial product.

```
poetry install
poetry shell
python pluginflow.py
```

Output is in `PluginFlow.pdf`.

## References
- [is-there-a-matplotlib-flowable-for-reportlab](https://stackoverflow.com/questions/4690585/is-there-a-matplotlib-flowable-for-reportlab/50765404#50765404)

