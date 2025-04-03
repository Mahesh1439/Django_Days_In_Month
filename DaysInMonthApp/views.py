from django.shortcuts import render

# Create your views here.
def day_in_a_month(request):
    days_in_month={
        "January":31,
        "February": "28/29",
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }
    return render(request,'template_html_files/daysInMonth.html',context=days_in_month)

