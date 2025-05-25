document.addEventListener('DOMContentLoaded', () => {
    // DOM Elements - Common
    const currentYearSpan = document.getElementById('current-year');
    const optionCards = document.querySelectorAll('.option-card');
    const sectionContainers = document.querySelectorAll('.section-container');
    
    // DOM Elements - Conversion
    const amountInput = document.getElementById('amount');
    const fromCurrencySelect = document.getElementById('from-currency');
    const toCurrencySelect = document.getElementById('to-currency');
    const swapButton = document.getElementById('swap-button');
    const convertButton = document.getElementById('convert-button');
    const conversionResultContainer = document.getElementById('conversion-result-container');
    const conversionResultValue = document.getElementById('conversion-result-value');
    const conversionExchangeRate = document.getElementById('conversion-exchange-rate');
    const conversionTimestamp = document.getElementById('conversion-timestamp');
    
    // DOM Elements - Exchange Rate
    const baseCurrencySelect = document.getElementById('base-currency');
    const targetCurrencySelect = document.getElementById('target-currency');
    const rateSwapButton = document.getElementById('rate-swap-button');
    const getRateButton = document.getElementById('get-rate-button');
    const rateResultContainer = document.getElementById('rate-result-container');
    const rateResultValue = document.getElementById('rate-result-value');
    const rateTimestamp = document.getElementById('rate-timestamp');

    // Set current year in footer
    currentYearSpan.textContent = new Date().getFullYear();

    // Navigation
    optionCards.forEach(card => {
        card.addEventListener('click', () => {
            // Remove active class from all cards and sections
            optionCards.forEach(c => c.classList.remove('active'));
            sectionContainers.forEach(s => s.classList.remove('active'));
            
            // Add active class to clicked card
            card.classList.add('active');
            
            // Show corresponding section
            const sectionId = card.getAttribute('data-section');
            document.getElementById(sectionId).classList.add('active');
        });
    });

    // Set first option as active by default
    optionCards[0].click();

    // Event Listeners - Conversion
    swapButton.addEventListener('click', swapCurrencies);
    convertButton.addEventListener('click', performConversion);
    amountInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            performConversion();
        }
    });

    // Event Listeners - Exchange Rate
    rateSwapButton.addEventListener('click', swapRateCurrencies);
    getRateButton.addEventListener('click', getExchangeRate);

    // Initial focus
    amountInput.focus();

    // Functions - Conversion
    function swapCurrencies() {
        const tempCurrency = fromCurrencySelect.value;
        fromCurrencySelect.value = toCurrencySelect.value;
        toCurrencySelect.value = tempCurrency;
        
        // Animate the swap button
        swapButton.classList.add('rotate');
        setTimeout(() => {
            swapButton.classList.remove('rotate');
        }, 500);

        // If there's already a result, update the conversion
        if (!conversionResultContainer.classList.contains('hidden')) {
            performConversion();
        }
    }

    // Functions - Exchange Rate
    function swapRateCurrencies() {
        const tempCurrency = baseCurrencySelect.value;
        baseCurrencySelect.value = targetCurrencySelect.value;
        targetCurrencySelect.value = tempCurrency;
        
        // Animate the swap button
        rateSwapButton.classList.add('rotate');
        setTimeout(() => {
            rateSwapButton.classList.remove('rotate');
        }, 500);

        // If there's already a result, update the rate
        if (!rateResultContainer.classList.contains('hidden')) {
            getExchangeRate();
        }
    }

    function performConversion() {
        const amount = amountInput.value;
        const fromCurrency = fromCurrencySelect.value;
        const toCurrency = toCurrencySelect.value;

        // Validate input
        if (!amount || isNaN(amount) || amount <= 0) {
            showError('Please enter a valid amount');
            return;
        }

        // Show loading state
        convertButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Converting...';
        convertButton.disabled = true;

        // API request
        fetch('/convert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                amount,
                from_currency: fromCurrency,
                to_currency: toCurrency
            })
        })
        .then(response => response.json())
        .then(data => {
            // Reset button state
            convertButton.innerHTML = '<i class="fas fa-calculator"></i> Convert';
            convertButton.disabled = false;

            if (data.success) {
                displayConversionResult(data.result);
            } else {
                showError(data.error || 'An error occurred during conversion');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            convertButton.innerHTML = '<i class="fas fa-calculator"></i> Convert';
            convertButton.disabled = false;
            showError('Network error. Please try again later.');
        });
    }

    function displayConversionResult(result) {
        // Format result
        const formattedAmount = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: result.from_currency,
            currencyDisplay: 'code'
        }).format(result.amount);

        const formattedConvertedAmount = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: result.to_currency,
            currencyDisplay: 'code'
        }).format(result.converted_amount);

        // Update DOM
        conversionResultValue.textContent = `${formattedAmount} = ${formattedConvertedAmount}`;
        conversionExchangeRate.textContent = `1 ${result.from_currency} = ${result.rate} ${result.to_currency}`;
        conversionTimestamp.textContent = `Last updated: ${new Date().toLocaleString()}`;
        
        // Show result container with animation
        conversionResultContainer.classList.remove('hidden');
        conversionResultContainer.style.opacity = 0;
        setTimeout(() => {
            conversionResultContainer.style.opacity = 1;
        }, 10);
    }

    // Functions - Exchange Rate
    function getExchangeRate() {
        const baseCurrency = baseCurrencySelect.value;
        const targetCurrency = targetCurrencySelect.value;

        // Show loading state
        getRateButton.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Loading...';
        getRateButton.disabled = true;

        // API request
        fetch('/get_rate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                from_currency: baseCurrency,
                to_currency: targetCurrency
            })
        })
        .then(response => response.json())
        .then(data => {
            // Reset button state
            getRateButton.innerHTML = '<i class="fas fa-sync-alt"></i> Get Exchange Rate';
            getRateButton.disabled = false;

            if (data.success) {
                displayRateResult(data.result);
            } else {
                showError(data.error || 'An error occurred while fetching the exchange rate');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            getRateButton.innerHTML = '<i class="fas fa-sync-alt"></i> Get Exchange Rate';
            getRateButton.disabled = false;
            showError('Network error. Please try again later.');
        });
    }

    function displayRateResult(result) {
        // Update DOM
        rateResultValue.textContent = `1 ${result.from_currency} = ${result.rate} ${result.to_currency}`;
        rateTimestamp.textContent = `Last updated: ${new Date().toLocaleString()}`;
        
        // Show result container with animation
        rateResultContainer.classList.remove('hidden');
        rateResultContainer.style.opacity = 0;
        setTimeout(() => {
            rateResultContainer.style.opacity = 1;
        }, 10);
    }

    // Common Functions
    function showError(message) {
        // We could add a nicer error UI here, but for now, use alert
        alert(message);
    }
}); 