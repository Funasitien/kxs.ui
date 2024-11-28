class Draw:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.body = ""
        self.police = ""
        self.template = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {} {}">
\t{}
</svg>"""
        self.template_police = """<defs>
\t\t<style>
\t\t\t{}
\t\t</style>
\t</defs>
\t"""
        
    def generate(self):
        """
            CrÃ©e le svg.
        """
        if self.police != "":
            self.body = self.template_police.format(self.police.strip()) + self.body
        return self.template.format(self.width, self.height, self.body.strip())
    
    def output(self):
        """
            Affiche le code de l'image dans le shell
        """
        print(self.generate())

    def save(self, filename):
        """
            Enregistre l'image dans le fichier filename
        """
        f = open(filename, 'w')
        f.write(self.generate())
        f.close()
    
    def addPolice(self, url):
        """
            Ajoute une police grÃ¢ce Ã  son url dans Google font.
            Il faut aller sur cette url https://fonts.google.com sÃ©lectionner
            une police et rÃ©cupÃ©rer l'url dans le @import.
        """
        t = '@import url("{}");'
        self.police += t.format(url.replace("&","&amp;")) + "\n\t\t\t"
    
    def rectangle(self, x, y, width, height, stroke = "", strokewidth = "", fill = ""):
        """
            Trace un rectangle.
            
            x : abscisse du point haut gauche
            y : ordonnÃ©e du point haut gauche
            width : largeur du rectangle
            height : hauteur de rectangle
            stroke : couleur du trait (dÃ©faut : none)
            strokewidth : Ã©paisseur de trait (dÃ©faut : 1px)
            fill : couleur de remplissage (dÃ©faut : none)
        """
        
        t = '<rect x="{}" y="{}" width="{}" height="{}"{}/>'
        
        style_content = ""
        if stroke != "":
            style_content += ' stroke: ' + stroke + ';'
        if strokewidth != "":
            style_content += ' stroke-width: ' + str(strokewidth) + ';'
        if fill != "":
            style_content += ' fill: ' + fill + ';'
            
        if style_content != "":
            style= ' style="' + style_content[1:] + '"'
        else:
            style = ""
        
        self.body += t.format(x, y, width, height, style) + "\n\t"
        
        
    def line(self, x1, y1, x2, y2, stroke = "", strokewidth = ""):
        """
            Trace une ligne.
            
            x1 : abscisse du premier point
            y1 : ordonnÃ©e du premier point
            x2 : abscisse du deuxiÃ¨me point
            y2 : ordonnÃ©e du deuxiÃ¨me point
            stroke : couleur du trait (dÃ©faut : none)
            strokewidth : Ã©paisseur de trait (dÃ©faut : 1px)
        """
            
        t = '<line x1="{}" y1="{}" x2="{}" y2="{}"{}/>'
         
        style_content = ""
        if stroke != "":
            style_content += ' stroke: ' + stroke + ';'
        if strokewidth != "":
            style_content += ' stroke-width: ' + str(strokewidth) + ';'
            
        if style_content != "":
            style= ' style="' + style_content[1:] + '"'
        else:
            style = ""
    
        self.body += t.format(x1, y1, x2, y2, style) + "\n\t"
    
    
    def circle(self, cx, cy, r, stroke = "", strokewidth = "", fill = ""):
        """
            Trace un cercle.
            
            cx : abscisse du centre
            cy : ordonnÃ©e du centre
            stroke : couleur du trait (dÃ©faut : none)
            strokewidth : Ã©paisseur de trait (dÃ©faut : 1px)
            fill : couleur de remplissage (dÃ©faut : none)
        """
        
        t = '<circle cx="{}" cy="{}" r="{}"{}/>'
        
        style_content = ""
        if stroke != "":
            style_content += ' stroke: ' + stroke + ';'
        if strokewidth != "":
            style_content += ' stroke-width: ' + str(strokewidth) + ';'
        if fill != "":
            style_content += ' fill: ' + fill + ';'
            
        if style_content != "":
            style= ' style="' + style_content[1:] + '"'
        else:
            style = ""
        
        self.body += t.format(cx, cy, r, style) + "\n\t"    
        
    
    
    
    
    
    def text(self, x, y, s, stroke = "", strokewidth = "", fill = "", fontsize = "", fontfamily = "", textanchor = "", rotate = ""):
        """
            Ã‰crit un texte.
            
            x : abscisse du point en bas Ã  gauche du texte
            y : ordonnÃ©e du point en bas Ã  gauche du texte
            s : le texte Ã  afficher
            stroke : couleur du trait (dÃ©faut : #000000)
            strokewidth : Ã©paisseur de trait (dÃ©faut : 1px)
            fill : couleur de remplissage (dÃ©faut : none)
            fontsize : taille de police (dÃ©faut : 16px)
            fontfamily : police
            textanchor : position d'attache du texte en abscisse (start | middle | end; dÃ©faut : start)
            rotate : angle de rotation du texte par rapport au point d'attache. Sens trigonomÃ©trique.
        """
        
        
        t='<text x="{}" y="{}"{}{}>{}</text>'
        
        style_content = ""
        if stroke != "":
            style_content += ' stroke: ' + stroke + ';'
        if strokewidth != "":
            style_content += ' stroke-width: ' + str(strokewidth) + ';'
        if fill != "":
            style_content += ' fill: ' + fill + ';'
        if fontsize != "":
            style_content += ' font-size: ' + fontsize + ';'
        if fontfamily != "":
            style_content += ' font-family: ' + fontfamily + ';'
        if textanchor != "":
            style_content += ' text-anchor: ' + textanchor + ';'
        
        if rotate != "":
            rotate = - int(rotate)
            transform = ' transform="rotate(' + str(rotate) + ',' + str(x) + ',' + str(y) + ')"'
        else:
            transform = ""
        
        if style_content != "":
            style= ' style="' + style_content[1:] + '"'
        else:
            style = ""
        
        self.body += t.format(x, y, transform, style, s) + "\n\t"
        
if __name__ == "__main__":   
    test = Draw(200,150)
    #test.rectangle(10,10,50,30, "#EE55EE", 2, "#0055EE")
    #test.rectangle(0,0,20,30, "#222222", 2, "#EE0000")
    #test.line(100,50,150,50,"#000000")
    test.circle(50,50,30, "#111111", 1, "red")
    test.addPolice("https://fonts.googleapis.com/css?family=Open+Sans&display=swap")
    test.addPolice("https://fonts.googleapis.com/css2?family=Zen+Dots&display=swap")
    test.addPolice("https://fonts.googleapis.com/css2?family=RocknRoll+One&display=swap")
    test.text(10,20,"Azertyuiop", "", "", "#222222", "20px")
    test.text(10,40,"Azertyuiop", "", "", "#222222", "20px", "Arial")
    test.text(10,60,"Azertyuiop", "", "", "#222222", "20px", "Verdana")
    test.text(10,80,"Azertyuiop", "", "", "#222222", "20px", "'open sans'")
    test.text(10,100,"Azertyuiop", "", "", "#222222", "20px", "zen dots")
    test.text(10,120,"Azertyuiop", "", "", "#222222", "20px", "RocknRoll One")
    test.output()
    test.save("toto.svg")
