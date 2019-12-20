{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Summary Functions\n",
    "\n",
    "def get_summ_combined_county_annual(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns seller details such as addresses\n",
    "\n",
    "        >>>get_summ_combined_county_annual('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'combined_county_annual?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        combined_county_annual_df = json_normalize(requests.get(full_url).json())\n",
    "        return combined_county_annual_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "        \n",
    "def get_summ_combined_county_monthly(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns seller details such as addresses\n",
    "\n",
    "        >>>get_summ_combined_county_monthly('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'combined_county_monthly?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        combined_county_monthly_df = json_normalize(requests.get(full_url).json())\n",
    "        return combined_county_monthly_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_pharmacies_county(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all pharmacy totals by county (Will be large and could take extra time to load)\n",
    "\n",
    "        >>>get_summ_total_pharmacies_county('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_pharmacies_county?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_pharmacies_county_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_pharmacies_county_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_manufacturers_county(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all Manufacturer totals by county (Will be large and could take extra time to load)\n",
    "\n",
    "        >>>get_summ_total_manufacturers_county('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_manufacturers_county?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_manufacturers_county_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_manufacturers_county_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_distributors_county(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all Distributor totals by county (Will be large and could take extra time to load)\n",
    "\n",
    "        >>>get_summ_total_distributors_county('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_distributors_county?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_distributors_county_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_distributors_county_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_pharmacies_state(state,verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all pharmacy totals by state (Will be large and could take extra time to load)\n",
    "\n",
    "        >>>get_summ_total_pharmacies_state('OH')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_pharmacies_state?'\n",
    "    add_state = 'state=' + state\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_pharmacies_state_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_pharmacies_state_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_manufacturers_state(state,verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all Manufacturer totals by state (Will be large and could take extra time to load) \n",
    "\n",
    "        >>>get_summ_total_manufacturers_state('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_manufacturers_state?'\n",
    "    add_state = 'state=' + state\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_manufacturers_state_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_manufacturers_state_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_total_distributors_state(state,verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns all Distributor totals by state (Will be large and could take extra time to load) \n",
    "\n",
    "        >>>get_summ_total_distributors_state('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'total_distributors_state?'\n",
    "    add_state = 'state=' + state\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        total_distributors_state_df = json_normalize(requests.get(full_url).json())\n",
    "        return total_distributors_state_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL and state are correct: ', full_url)\n",
    "\n",
    "def get_summ_combined_buyer_annual(state, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns summarized annual dosages of pharmacies and practitioners by state and county \n",
    "\n",
    "        >>>get_summ_combined_buyer_annual('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'combined_buyer_annual?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        combined_buyer_annual_df = json_normalize(requests.get(full_url).json())\n",
    "        return combined_buyer_annual_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        \n",
    "def get_summ_combined_buyer_monthly(state, year, county = '',verification = True, key = 'WaPo'):\n",
    "    '''(str(two letter abbreviation), str, bool, str) -> pd.df\n",
    "        Returns dosages by pharmacy or practitioner by county, state, and yea \n",
    "\n",
    "        >>>get_summ_combined_buyer_monthly('OH', 'Summit')\n",
    "            EXAMPLE OUTPUT\n",
    "    '''\n",
    "\n",
    "    base_url = 'https://arcos-api.ext.nile.works/v1/'\n",
    "    function_url = 'combined_buyer_monthly?'\n",
    "    add_state = 'state=' + state\n",
    "    add_county = '&county=' + county\n",
    "    add_year = '&year=' + year\n",
    "    add_key = '&key=' + key\n",
    "    full_url = base_url + function_url + add_state + add_county + add_year + add_key\n",
    "\n",
    "    if verification == True:\n",
    "        print(full_url)\n",
    "        combined_buyer_monthly_df = json_normalize(requests.get(full_url).json())\n",
    "        return combined_buyer_monthly_df\n",
    "    else:\n",
    "        print('Problem encountered, not returning data:')\n",
    "        print('Either verification == False')\n",
    "        print('Or problem with API encountered, please verify URL, state and county are correct: ', full_url)\n",
    "        "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
