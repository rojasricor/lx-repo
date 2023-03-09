#!/usr/bin/env ruby
 
# Importamos dependendecias de 'FXruby' 
require 'fox16'
require 'fox16/scintilla'
 
 
include Fox
 
class ScintillaTest  < FXMainWindow
 
  def initialize(app)
 
    # Llamamos al método que inicializa la clase base
    super(app, "Lector Simple de Archivos HTML", nil, nil, DECOR_ALL, 0, 0, 600, 800)
 
    # Creamos una barra de menú 
    menubar = FXMenuBar.new(self, LAYOUT_SIDE_TOP|LAYOUT_FILL_X)
 
    # Creamos una barra de estado 
    FXStatusBar.new(self,
      LAYOUT_SIDE_BOTTOM|LAYOUT_FILL_X|STATUSBAR_WITH_DRAGCORNER)
 
    # El widget Scintilla de FXRuby ocupa el resto del espacio 
    sunkenFrame = FXHorizontalFrame.new(self,
      FRAME_SUNKEN|FRAME_THICK|LAYOUT_FILL_X|LAYOUT_FILL_Y)
    @scintilla = FXScintilla.new(sunkenFrame, nil, 0, LAYOUT_FILL_X|LAYOUT_FILL_Y)
 
 
    # Opción del Menú para Abrir archivos HTML en una ventana de selección de archivos HTML  
    filemenu = FXMenuPane.new(self)
    FXMenuCommand.new(filemenu, "&Abrir\tCtl-O\tOpen...").connect(SEL_COMMAND) {
      openDialog = FXFileDialog.new(self, "Abrir Archivo")
      openDialog.selectMode = SELECTFILE_EXISTING
      openDialog.patternList = ["Archivos HTML (*.html)"]
      if openDialog.execute != 0
        loadFile(openDialog.filename)
      end
    }
 
    # Creamos el menú Archivo 
    FXMenuTitle.new(menubar, "&Archivo", nil, filemenu)
 
 
    # Opción del Menú para para Salir del Programa 
    FXMenuCommand.new(filemenu, "&Salir\tCtl-Q\tQuit application.", nil,
      getApp(), FXApp::ID_QUIT, 0)  
 
    # Opciones del Menu Ayuda
    helpmenu = FXMenuPane.new(self)    
    FXMenuCommand.new(helpmenu, "&Web...").connect(SEL_COMMAND) {
      
      # Abrimos el enlace en el navegador 
      url = "https://nubecolectiva.com/"
      
      if RbConfig::CONFIG['host_os'] =~ /mswin|mingw|cygwin/
        system "start #{url}"
      elsif RbConfig::CONFIG['host_os'] =~ /darwin/
        system "open #{url}"
      elsif RbConfig::CONFIG['host_os'] =~ /linux|bsd/
        system "xdg-open #{url}"
      end
 
    }
 
    # Creamos el Menú Ayuda  
    FXMenuTitle.new(menubar, "&Ayuda", nil, helpmenu, LAYOUT_RIGHT)
    
  end
 
  # Abrimos el archivo HTML 
  def loadFile(filename)
    getApp().beginWaitCursor do
      text = File.open(filename, "r").read
      @scintilla.setText(text)
    end
  end
 
  # Creamos el espacio para el lector de archivos HTML 
  def create
    super
    show(PLACEMENT_SCREEN)
  end
end
 
if __FILE__ == $0
  # Construimos la aplicación 
  application = FXApp.new("ScintillaTest", "FoxTest")
 
  # Creamos la ventana para la aplicación 
  ScintillaTest.new(application)
 
  # Creamos la aplicación 
  application.create
 
  # Corremos la aplicación 
  application.run
end