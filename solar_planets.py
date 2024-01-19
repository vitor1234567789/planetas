import cv2

img = cv2.imread("solar_system.jpg")

# Add text to the image
cv2.putText(img,
            "Sol",
            (100, 80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0, 0, 255)
            )

# Display the modified image with the added text
cv2.imshow("resultado", img)

# Wait for a key event and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the modified image with the added text
cv2.imwrite("solar_system.jpg", img)