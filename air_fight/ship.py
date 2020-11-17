import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        # 记载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_recct = screen.get_rect()
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_recct.centerx
        self.rect.bottom = self.screen_recct.bottom
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的未知'''
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        elif self.moving_up:
            self.rect.centery -= 1
        elif self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        '''在指定未知绘制飞船'''
        self.screen.blit(self.image, self.rect)
