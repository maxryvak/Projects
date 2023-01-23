import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "ARvorgzU6nlaqL6Oaaa1lcGuwjC22as0f_yoHWCb6bSHIb_O8bci2U1K_g6qCBbzFG34uhLNGyx4n4bw"
        self.client_secret = "EAlayuyT5-SxPIuuOy3SytcWNvWLiZ3W1fO05DYTN978Sx8ANs2vUIIK_FFoDQiaupjWRDCWeIvK4tSn"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)

        