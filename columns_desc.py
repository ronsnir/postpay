columns_dict = {
    "instalment_plan_id": {
        "description": "Instalment plan ID",
        "type": "integer",
        "class": "id",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "customer_id": {
        "description": "Customer ID",
        "type": "numeric",
        "class": "id",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "order_id": {
        "description": "Order unique ID",
        "type": "integer",
        "class": "id",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "created": {
        "description": "Order created date",
        "type": "date",
        "class": "date",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "payment_method_brand": {
        "description": "Card brand: mastercard, visa, etc.",
        "type": "object",
        "class": "categorical",
        "missing_values": "None",
        "nulls_method": "CategoricalImputer_Missing",
        "imputer": "None",
    },
    "payment_method_expires": {
        "description": "Card expiration date",
        "type": "date",
        "class": "date",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "days_forward",
    },
    "total_amount": {
        "description": "Order amount",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "merchant_name": {
        "description": "Merchant name",
        "type": "object",
        "class": "categorical",
        "missing_values": "None",
        "nulls_method": "CategoricalImputer_Missing",
        "imputer": "None",
    },
    "checkout_type": {
        "description": "Checkout type - Shopping App, Browser",
        "type": "object",
        "class": "categorical",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "payment_method_type": {
        "description": "Card type - Credit, Debit",
        "type": "object",
        "class": "categorical",
        "missing_values": "None",
        "nulls_method": "CategoricalImputer_Missing",
        "imputer": "None",
    },
    "nr_of_items": {
        "description": "Number of items in the cart",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "unpaid_at_30": {
        "description": "TARGET - Unpaid classification - 1 for unpaid amount at 30 > 0 ; 0 for unpaid amount at 30 = 0",
        "type": "integer",
        "class": "numeric",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    "customer_first_joined": {
        "description": "Customer first joined date",
        "type": "date",
        "class": "date",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "days_back",
    },
    "date_of_birth": {
        "description": "Customer date of birth",
        "type": "date",
        "class": "date",
        "missing_values": "Optional field",
        "nulls_method": "None",
        "imputer": "years_back",
    },
    "avg_order_value": {
        "description": "Customer average order value",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "None",
        "nulls_method": "ArbitraryNumberImputer_0",
        "imputer": "None",
    },
    "avg_fees_per_order_365d": {
        "description": "Customer average fees - past 365 days",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "No fees",
        "nulls_method": "ArbitraryNumberImputer_0",
        "imputer": "None",
    },
    # "avg_fees_per_order_180d": {
    #     "description": "Customer average fees - past 180 days",
    #     "type": "numeric",
    #     "class": "numeric",
    #     "missing_values": "No fees",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "avg_fees_per_order_90d": {
    #     "description": "Customer average fees - past 90 days",
    #     "type": "numeric",
    #     "class": "numeric",
    #     "missing_values": "No fees",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "avg_fees_per_order_30d": {
    #     "description": "Customer average fees - past 30 days",
    #     "type": "numeric",
    #     "class": "numeric",
    #     "missing_values": "No fees",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    "count_merchants_per_customer": {
        "description": "Customer number of merchants shpped with",
        "type": "numeric",
        "class": "integer",
        "missing_values": "None",
        "nulls_method": "None",
        "imputer": "None",
    },
    # "count_open_orders": {
    #     "description": "Customer number of orders with status: 'due'",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No open orders",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "count_paid_orders": {
    #     "description": "Customer number of paid orders",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No paid orders",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "count_unpaid_orders": {
    #     "description": "Customer number of unpaid orders",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No unpaid orders",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "count_paid_instalments": {
    #     "description": "Customer number of paid instalments",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No paid instalments",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    # "count_unpaid_instalments": {
    #     "description": "Customer number of unpaid instalments",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No unpaid instalments",
    #     "nulls_method": "ArbitraryNumberImputer_0",
    #     "imputer": "None",
    # },
    "current_exposure": {
        "description": "The sum of outstanding captured debt",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "No open orders",
        "nulls_method": "ArbitraryNumberImputer_0",
        "imputer": "None",
    },
    "sum_paid_amount": {
        "description": "Customer total paid amount",
        "type": "numeric",
        "class": "numeric",
        "missing_values": "No paid orders",
        "nulls_method": "ArbitraryNumberImputer_0",
        "imputer": "None",
    },
    # "days_since_last_unpaid": {
    #     "description": "Customer amount of days since the last unpaid instalment",
    #     "type": "numeric",
    #     "class": "integer",
    #     "missing_values": "No unpaid orders",
    #     "nulls_method": "None",
    #     "imputer": "None",
    # },
    "user_agent_type": {
        "description": "Customer device type - 'iPhone', 'Windows NT', 'Macintosh', 'Android'",
        "type": "object",
        "class": "categorical",
        "missing_values": "Missing device type",
        "nulls_method": "CategoricalImputer_Missing",
        "imputer": "None",
    },
}
