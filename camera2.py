import cv2
import numpy as np


# Funkcja do przetwarzania klatki wideo
def process_frame(frame):
    # Konwersja obrazu do przestrzeni kolorów HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Wybór zakresu kolorów reprezentujących uschniętą trawę w przestrzeni HSV
    lower_bound = np.array([20, 50, 50])  # Minimalne wartości odcienia, nasycenia i jasności
    upper_bound = np.array([40, 255, 255])  # Maksymalne wartości odcienia, nasycenia i jasności

    # Utworzenie maski na podstawie wybranego zakresu kolorów
    mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

    # Przykład: Wyświetlenie oryginalnej klatki obrazu i maski
    combined = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Combined', combined)

    return frame  # Możesz zwrócić przetworzoną klatkę lub cokolwiek innego


# Wczytanie źródła wideo (możesz zmienić '0' na nazwę pliku wideo, jeśli korzystasz z pliku)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    processed_frame = process_frame(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
