function MTA(expectedProfit, maximumLoss, amount, size, totalProfit){

if (!expectedProfit){
    expectedProfit = input('Expected Profit');
}
if (!maximumLoss){
    maximumLoss = input('Maximum Loss Amount');
}
if (!amount){
    amount = input('Trade Amount');
}
if (!size){
    size = 1;
}
if (!totalProfit){
    totalProfit = 0;
}
return size * amount

}