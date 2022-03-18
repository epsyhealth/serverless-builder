from serverless.service.plugins.generic import Generic


class AWSCodeSign(Generic):
    yaml_tag = "!AWSSignPlugin"

    def __init__(
        self,
        profile,
        sign_policy="Enforce",
        source_bucket=None,
        source_key=None,
        desitnation_bucket=None,
        destination_prefix=None,
        retain=False,
    ):
        super().__init__("serverless-aws-signer")
        self.profile = profile
        self.sign_policy = sign_policy
        self.source_bucket = source_bucket
        self.source_key = source_key
        self.destination_bucket = desitnation_bucket
        self.destination_prefix = destination_prefix
        self.retain = retain

    def enable(self, service):
        service.custom.signer = dict(
            retain=self.retain,
            source=dict(s3=dict(bucketName=self.source_bucket, key=self.source_key)),
            destination=dict(s3=dict(bucketName=self.destination_bucket, prefix=self.destination_prefix)),
            profileName=self.profile,
            signingPolicy=self.sign_policy,
        )