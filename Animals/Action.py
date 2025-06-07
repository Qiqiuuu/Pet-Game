import os

import pygame


class Action:
    """
    Klasa Action zarządza sekwencją animacji, taką jak pojawienie się butelek z jedzeniem
    lub serc po interakcji ze zwierzakiem. Obsługuje ładowanie klatek animacji,
    ich odtwarzanie i rysowanie na ekranie.
    """
    def __init__(self, pet, numFrames: int, y: float, path: str):
        """
        Ładuje wszystkie klatki animacji na podstawie podanej ścieżki i liczby klatek.
        Skaluje klatki w oparciu o rozmiar prostokąta zwierzaka.

        :param pet: Obiekt zwierzaka (np. instancja `Cow`, `Cat` itp.), do którego odnosi się akcja.
                    Używany do skalowania animacji i pozycjonowania.
        :param numFrames: Całkowita liczba klatek w sekwencji animacji.
        :type numFrames: int
        :param y: Offset Y dla rysowania animacji względem górnej krawędzi zwierzaka.
        :type y: float
        :param path: Ścieżka bazowa do plików graficznych klatek (np. "bottles" lub "heart").
                     Używana do konstruowania pełnych ścieżek plików.
        :type path: str
        """
        self.pet = pet
        self.frames = []
        self.numFrames = numFrames
        self.frameDuration = pet.animationSpeed
        self.y = y
        self.path = path
        self.currentFrameIndex = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.isPlaying = False
        self.hasFinished = False

        scriptDir = os.path.dirname(os.path.abspath(__file__))
        if self.path.startswith("bottles"):
            assetsBasePath = os.path.join(scriptDir, 'Pets', 'Assets', 'Bottles')
        elif self.path.startswith("heart"):
            assetsBasePath = os.path.join(scriptDir, 'Pets', 'Assets', 'Hearts')
        for i in range(1, numFrames + 1):
            imageFilename = f"{self.path}{i}.png"
            fullImagePath = os.path.join(assetsBasePath, imageFilename)
            img = pygame.image.load(fullImagePath).convert_alpha()
            img = pygame.transform.scale(img, (self.pet.rect.width * 7, self.pet.rect.height * 7))
            self.frames.append(img)

    def Start(self):
        """
        Rozpoczyna odtwarzanie animacji.

        Resetuje indeks klatki do 0, ustawia flagi `isPlaying` na True
        i `hasFinished` na False, oraz aktualizuje czas ostatniej aktualizacji.
        """
        self.isPlaying = True
        self.hasFinished = False
        self.currentFrameIndex = 0
        self.lastUpdate = pygame.time.get_ticks()

    def Update(self):
        """
        Aktualizuje stan animacji, przechodząc do następnej klatki, jeśli upłynął
        odpowiedni czas.

        Jeśli animacja nie jest odtwarzana lub już się zakończyła, metoda nie wykonuje żadnych działań.
        Po osiągnięciu ostatniej klatki, animacja zostaje zakończona.
        """
        if not self.isPlaying or self.hasFinished:
            return
        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastUpdate > self.frameDuration:
            self.currentFrameIndex += 1
            self.lastUpdate = currentTime

            if self.currentFrameIndex >= len(self.frames):
                self.hasFinished = True
                self.isPlaying = False
                self.currentFrameIndex = len(self.frames) - 1

    def Draw(self, screen: pygame.Surface):
        """
        Rysuje aktualną klatkę animacji na ekranie.

        Animacja jest rysowana tylko wtedy, gdy jest odtwarzana.
        Animacja nie jest rysowana, jeśli zakończyła się i aktualny indeks to ostatnia klatka.
        Pozycja rysowania jest obliczana względem środka prostokąta zwierzaka i offsetu Y.

        :param screen: Powierzchnia Pygame, na której ma zostać narysowana animacja.
        :type screen: pygame.Surface
        """
        if not self.isPlaying and not self.hasFinished:
            return
        if self.hasFinished and self.currentFrameIndex == len(self.frames) - 1:
            return
        if len(self.frames) > 0 and 0 <= self.currentFrameIndex < len(self.frames):
            currentImage = self.frames[self.currentFrameIndex]
            drawX = self.pet.rect.centerx - currentImage.get_width() // 2
            drawY = self.pet.rect.top - self.y
            screen.blit(currentImage, (drawX, drawY))
