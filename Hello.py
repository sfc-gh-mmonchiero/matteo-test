# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Datasets",
        page_icon="👋",
    )

    st.write("# Datasets Playground! 👋")
 
    
    st.markdown("""***Example***\n
    SELECT i.cik, i.company_name, r.period_start_date, r.period_end_date, r.measure_description, TO_NUMERIC(r.value) AS value
    FROM cybersyn.sec_cik_index AS i
    JOIN cybersyn.sec_report_attributes AS r ON (r.cik = i.cik)
    WHERE i.sic_code_description = 'AIR TRANSPORTATION, SCHEDULED'
      AND r.statement = 'Income Statement'
      AND r.period_end_date = '2022-12-31'
      AND r.covered_qtrs = 4
      AND r.metadata IS NULL
      AND r.measure_description IN ('Total operating revenues', 'Total operating revenue');""")
    
    
    conn = st.connection("snowflake")
    command = st.text_area('Input SQL')
    if command:
        query = conn.query(command)
        st.dataframe(query)

if __name__ == "__main__":
    run()
