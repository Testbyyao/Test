import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--tenant_id",
        type=str,
        required=True,
        help="The tenant id of the service principal",
    )
    parser.add_argument(
        "--client_id",
        type=str,
        required=True,
        help="The client id of the service principal",
    )
    parser.add_argument(
        "--client_secret",
        type=str,
        required=True,
        help="The client secret of the service principal",
    )
    parser.add_argument(
        "--secret_name",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--secret_value",
        type=str,
        required=True,
    )
    args = parser.parse_args()