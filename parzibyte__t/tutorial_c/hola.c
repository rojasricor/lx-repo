#include <stdio.h>
#include <stdlib.h>
#include <gtk/gtk.h>

int main(int argc, char *argv[])
{
    GtkWidget *window;
    GtkWidget *label;

    gtk_init(&argc, &argv);

    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    g_signal_connect(window, "delete-event", G_CALLBACK(gtk_main_quit), NULL);

    label = gtk_label_new("Hola mundo!");
    gtk_container_add(GTK_CONTAINER(window), label);

    gtk_widget_show_all(window);

    gtk_main();

    return 0;
}
