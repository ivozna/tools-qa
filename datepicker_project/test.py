"""
Test scenario:
1.Click on select date input.
2. Click on month select window.
3. Select a month.

4. Click and select a day.

5. Click on year select input.
6. Scroll and select a year.

7. Assert a desired date is selected.

8. Click navigation previous/next.
9. Assert a desired date is selected.
"""

from datetime import datetime


def test_datepicker(datepicker_page):
    datepicker_page.select_month('July')
    datepicker_page.select_year('2015')
    datepicker_page.select_day('23')
    assert datepicker_page.get_date() == '07/23/2015'


def test_datepicker_random(datepicker_page):
    datepicker_page.select_year('1993')
    datepicker_page.select_month('July')
    datepicker_page.select_day('23')
    assert datepicker_page.get_date() == '07/23/1993'


def test_date_next_previous(datepicker_page):
    assert datepicker_page.get_date() == datetime.today().strftime('%m/%d/%Y')
    datepicker_page.select_month_next()
    assert datepicker_page.get_current_month() == 'February 2022'
    datepicker_page.select_month_previous()
    assert datepicker_page.get_current_month() == 'January 2022'


def test_dateandtime(dateandtime_page):
    dateandtime_page.select_month('September')
    dateandtime_page.select_year(2030)
    dateandtime_page.select_day('17')
    dateandtime_page.select_time('15:00')
    assert dateandtime_page.get_dateandtime() == 'September 17, 2030 3:00 PM'
