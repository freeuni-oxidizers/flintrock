import os
import pytest

# Flintrock
from flintrock.core import (
    generate_template_mapping,
    get_formatted_template,
)

FLINTROCK_ROOT_DIR = (
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__))))


@pytest.mark.parametrize(
    'spark_version', [
        (''),
        ('3.3.0'),
        ('a28880f3b9c63d86368bcd6cbbaa6a9af7075409'),
    ])
def test_templates(dummy_cluster, spark_version):
    template_dir = os.path.join(FLINTROCK_ROOT_DIR, 'flintrock', 'templates')
    for (dirpath, dirnames, filenames) in os.walk(template_dir):
        if filenames:
            for filename in filenames:
                template_path = os.path.join(dirpath, filename)
                mapping = generate_template_mapping(
                    cluster=dummy_cluster,
                    hadoop_version='',
                    spark_version=spark_version,
                    spark_executor_instances=0,
                )
                get_formatted_template(
                    path=template_path,
                    mapping=mapping,
                )
