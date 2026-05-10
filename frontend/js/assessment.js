// ============================================================
// MINDGUARD — Assessment Form Handler
// ============================================================

const API_BASE = 'http://localhost:8000';

// ---------- Progress Bar ----------
const totalFields = 19;
const form = document.getElementById('assessmentForm');
const progressBar = document.getElementById('progressBar');
const resultsSection = document.getElementById('resultsSection');
const submitBtn = document.getElementById('submitBtn');
const submitText = document.getElementById('submitText');
const submitLoader = document.getElementById('submitLoader');

// Track filled fields
function updateProgress() {
    const inputs = form.querySelectorAll('input, select');
    let filled = 0;
    inputs.forEach(input => {
        if (input.value && input.value !== '') filled++;
    });
    const percent = (filled / totalFields) * 100;
    progressBar.style.width = percent + '%';
}

// Attach progress listeners
form.querySelectorAll('input, select').forEach(input => {
    input.addEventListener('change', updateProgress);
    input.addEventListener('input', updateProgress);
});

// ---------- Form Submission ----------
form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Show loader
    submitText.style.display = 'none';
    submitLoader.style.display = 'inline-block';
    submitBtn.disabled = true;

    // Collect form data
    const payload = {
        age: parseInt(document.getElementById('age').value),
        gender: document.getElementById('gender').value,
        relationship_status: document.getElementById('relationship_status').value,
        academic_status: document.getElementById('academic_status').value,
        work_and_study: document.getElementById('work_and_study').value,
        residential_area: document.getElementById('residential_area').value,
        social_economic_status: document.getElementById('social_economic_status').value,
        financial_pressure: document.getElementById('financial_pressure').value,
        has_debt: document.getElementById('has_debt').value,
        living_environment_satisfaction: document.getElementById('living_environment_satisfaction').value,
        recent_loss: document.getElementById('recent_loss').value,
        physical_activity: document.getElementById('physical_activity').value,
        chronic_illness: document.getElementById('chronic_illness').value,
        medication: document.getElementById('medication').value,
        smoking: document.getElementById('smoking').value,
        alcohol: document.getElementById('alcohol').value,
        sleep_duration_hours: document.getElementById('sleep_duration_hours').value,
        social_media_hours_daily: document.getElementById('social_media_hours_daily').value,
        academic_work_demands: document.getElementById('academic_work_demands').value
    };

    try {
        const response = await fetch(`${API_BASE}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Something went wrong');
        }

        const result = await response.json();
        displayResults(result);

    } catch (error) {
        alert('Error: ' + error.message + '\n\nPlease make sure the API server is running on port 8000.');
    } finally {
        submitText.style.display = 'inline';
        submitLoader.style.display = 'none';
        submitBtn.disabled = false;
    }
});

// ---------- Display Results ----------
function displayResults(result) {
    // Hide form, show results
    form.style.display = 'none';
    resultsSection.style.display = 'block';

    // Score
    const score = result.prediction.toFixed(1);
    document.getElementById('scoreValue').textContent = score;

    // Risk badge
    const risk = result.risk_level;
    const badge = document.getElementById('resultBadge');
    const riskSpan = document.getElementById('riskLevel');
    
    badge.className = 'result-badge';
    if (risk === 'Low') {
        badge.classList.add('low');
        riskSpan.textContent = '🟢 Low Risk';
    } else if (risk === 'Moderate') {
        badge.classList.add('moderate');
        riskSpan.textContent = '🟡 Moderate Risk';
    } else {
        badge.classList.add('high');
        riskSpan.textContent = '🔴 High Risk';
    }

    // Message
    document.getElementById('resultMessage').textContent = 
        result.response ? result.response.substring(0, 200) + '...' : 
        'See detailed insights below.';

    // Insights
    const insightsDiv = document.getElementById('resultInsights');
    insightsDiv.innerHTML = '';
    
    if (result.response) {
        const paragraphs = result.response.split('\n\n');
        paragraphs.forEach(para => {
            if (para.trim()) {
                const p = document.createElement('p');
                p.textContent = para.replace(/\*\*/g, '');
                insightsDiv.appendChild(p);
            }
        });
    }

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth' });
}