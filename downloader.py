from pytube import YouTube
import typer
from rich.console import Console
from rich.table import Table
import sys
import os
from typing import Optional



app = typer.Typer()
console = Console()

@app.command("url [Url Video YouTube] save_in[Path To Save Video Downloaded]")
def url(url: str, save_in: str, media: Optional[str] = typer.Argument("video")) -> None:
    console.print("\n[bold red] [!] Show Information... [/bold red]")
    
    youtube = YouTube(url)

    #! Draw Table with some information about video/audio downloaded
    table = Table(show_header=True)
    table.add_column("[deep_sky_blue3]Title[/deep_sky_blue3]", style="bold", min_width=20)
    table.add_column("[aquamarine1]Autor[/aquamarine1]", min_width=8, justify="center")
    table.add_column("[bold green]Views[/bold green]", min_width=7, justify="center")
    table.add_column("[bold red]Publish Date[/bold red]", min_width=8, justify="center")
    table.add_row(youtube.title, youtube.author, str(youtube.views), str(youtube.publish_date.date()))
    console.print(table)


    console.print("\n\n[bold blue] [+] Starting Download...(Be Patient) [/bold blue]\n")

    if (save_in == '.'):
        save_in = os.getcwd()

    if (media != "video" and media != "audio"):
        console.print("\n\n[bold red] [-] Media Not Available... [/bold red]\n")
        sys.exit(1)
    else:
        if (media == "video"):
            y_downloader = youtube.streams.get_highest_resolution()
            y_downloader.download(save_in)
        else:
            y_downloader = youtube.streams.get_audio_only()
            path_audio = y_downloader.download(save_in)
            base, _ = os.path.splitext(path_audio)
            new_path = base + ".mp3"
            os.rename(path_audio,new_path)

    console.print("\n[bold green] [+] Finished Download [/bold green]\n")


if __name__ == "__main__":
    app()