```python
from django.shortcuts import render
from .models import AffiliateAccount

def affiliate_account_list(request):
    accounts = AffiliateAccount.objects.all()
    return render(request, 'affiliates/account_list.html', {'accounts': accounts})

def affiliate_account_detail(request, pk):
    account = AffiliateAccount.objects.get(pk=pk)
    return render(request, 'affiliates/account_detail.html', {'account': account})

def affiliate_account_new(request):
    if request.method == "POST":
        form = AffiliateAccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('affiliate_account_detail', pk=account.pk)
    else:
        form = AffiliateAccountForm()
    return render(request, 'affiliates/account_edit.html', {'form': form})

def affiliate_account_edit(request, pk):
    account = AffiliateAccount.objects.get(pk=pk)
    if request.method == "POST":
        form = AffiliateAccountForm(request.POST, instance=account)
        if form.is_valid():
            account = form.save(commit=False)
            account.save()
            return redirect('affiliate_account_detail', pk=account.pk)
    else:
        form = AffiliateAccountForm(instance=account)
    return render(request, 'affiliates/account_edit.html', {'form': form})
```