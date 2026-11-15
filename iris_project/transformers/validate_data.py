
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def validate_data(df, *args, **kwargs):
    missing_values = df.isnull().sum().sum()
    number_of_classes = df["target"].nunique()

    print("Missing values:", missing_values)
    print("Number of classes:", number_of_classes)

    assert missing_values == 0, "Dataset contains missing values"
    assert number_of_classes == 3, "Iris dataset must contain exactly 3 classes"

    print("Validation successful!")
    return df


@test
def test_output(output, *args):
    assert output.isnull().sum().sum() == 0
    assert output["target"].nunique() == 3
