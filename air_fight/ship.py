import pygame


class Ship():
    def __init__(self, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        # 记载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_recct = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_recct.centerx
        self.rect.bottom = self.screen_recct.bottom

    def blitme(self):
        '''在指定未知绘制飞船'''
        self.screen.blit(self.image, self.rect)
