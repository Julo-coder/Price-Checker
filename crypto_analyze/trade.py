import token_data as td
import indicators
import patterns

user_token = input(str("Jaki token chcialbys przeanalizowac: "))
user_interval = input(str("Jaki interwał Ciebie interesuje (day, hour, minute): " ))
user_network = input(str("W jakiej sieci znajduje sie token (np. eth, ton, sol itp): "))

user_token_address = td.get_pools_address(td.get_pools_info(user_token))
user_analyze = td.get_ohlcvs_of_pool(user_token_address, user_network, user_interval)

print(user_analyze)
user_indicators = indicators.indicators(user_analyze)
print(user_indicators)