<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST'){
    header('Content-Type: application/json; charset=utf-8');
    
    $raw_input = file_get_contents('php://input');
    $decoded = json_decode($raw_input, true);
    $question = isset($decoded['question']) ? trim($decoded['question']) : '';

    if (empty($question)) {
        echo json_encode(['answer' => 'Otrzymałem puste zapytanie.']);
        exit;
    }

    $python_url = 'http://127.0.0.1:5050/ask'; 
    $payload = json_encode(['question' => $question]);

    $ch = curl_init($python_url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Content-Length: ' . strlen($payload)
    ]);
    curl_setopt($ch, CURLOPT_TIMEOUT, 15);

    $python_response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($python_response === false || $http_code !== 200) {
        echo json_encode(['answer' => '⚠️ Serwer AI aktualnie drzemie. Upewnij się w konsoli, czy skrypt Pythona jest uruchomiony.']);
        exit;
    }

    echo $python_response;
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="script.js" defer></script>
    <title>Eksperymentalny Doradca Emitujący Komunikaty</title>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">
            <h2>🤖 E.D.E.K</h2>
            <button id="theme-toggle" title="Zmień motyw">🌙</button>
        </div>
        
        <div class="chat-messages" id="chat-window">
            <div class="message bot-message">
                <p>Cześć, o co chcesz mnie dzisiaj zapytać?</p>
            </div>
        </div>
    
        <div class="chat-input-area">
            <input type="text" id="user-input" placeholder="Wpisz wiadomość..." autocomplete="off">
            <button id="send-btn">Wyślij</button>
        </div>
    </div>
</body>
</html>