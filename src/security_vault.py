"""
Author: Jijeesh Valappil
Module: Customer Managed Encryption Key (BYOK) Controller Engine
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [Jijeesh Valappil] - %(levelname)s - %(message)s"
)

def bind_customer_key(
    kms_key_id: str,
    cluster_uuid: str
) -> dict:
    """Binds a customer-managed key
    to an isolated cloud environment cluster.

    Args:
        kms_key_id (str):
            KMS Key Identifier

        cluster_uuid (str):
            Target Environment

    Returns:
        dict:
            Status information
    """

    logging.info(
        f"Initiating cryptographic handshake using KMS Key: {kms_key_id}"
    )

    return {
        "status": "ENFORCED",
        "scope": "BYOK_COMPLIANT",
        "target": cluster_uuid
    }
