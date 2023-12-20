import os
import flet as ft
from pytube import YouTube
import pyktok as pyk
pyk.specify_browser('chrome') 
import facebook_downloader as fd
import flet_fastapi







async def main(page: ft.Page):
    page.horizontal_alignment= "center"
    #Youtube Function
    async def yt_video_download(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        await page.update_async()
        yt = YouTube(url.value)
        yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        yt.download()
        url.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()
    async def yt_audio_download(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        await page.update_async()
        yt = YouTube(url.value)
        yt= yt.streams.filter(only_audio=True).first()
        out=yt.download()
        base, ext = os.path.splitext(out) 
        new_file = base + '.mp3'
        os.rename(out, new_file) 
        url.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()
    #tiktok function
    async def tik_download_video(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        await page.update_async()
        pyk.save_tiktok(url_tiktok.value)
        url_tiktok.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()
    async def tik_audio_download(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        page.update_async()
        tik=pyk.save_tiktok(url_tiktok.value)
        base, ext = os.path.splitext(tik) 
        new_file = base + '.mp3'
        os.rename(tik, new_file) 
        url_tiktok.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()
    #facebook function
    async def fb_download_video(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        await page.update_async()
        fd(url_face.value)
        url_face.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()
    async def fb_download_audio(e):
        down_progress.value ="Your File is Downloading Please Wait....."
        await page.update_async()
        fd(url_face.value)
        url_face.value =""
        down_progress.value =""   
        page.snack_bar.open = True
        await page.update_async()

    #download Progress    
    down_progress = ft.Text("")
    #logo
    logo = ft.Container(content=ft.Image(src="assets/logo2.png", width=600, height=200, fit=ft.ImageFit.CONTAIN))
    #Youtube
    url = ft.TextField(label="Type The Youtube Video URL Here", width=800, border_color="red")
    btn1 = ft.FloatingActionButton(icon=ft.icons.VIDEO_LIBRARY, text="Download Video", bgcolor="red", on_click=yt_video_download)
    btn2 = ft.FloatingActionButton(icon=ft.icons.AUDIOTRACK, text="Download Audio", bgcolor="red", on_click=yt_audio_download)
    row1 = ft.Row(controls=[logo], alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Row(controls=[url], alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row(controls=[btn1, btn2], alignment=ft.MainAxisAlignment.CENTER)
    #Tiktok
    url_tiktok = ft.TextField(label="Type The TikTok Video URL Here", width=800, border_color="white",)
    btn1_tiktok = ft.FloatingActionButton(icon=ft.icons.VIDEO_LIBRARY, text="Download Video", bgcolor="black", on_click=tik_download_video)
    btn2_tiktok = ft.FloatingActionButton(icon=ft.icons.AUDIOTRACK, text="Download Audio", bgcolor="black", on_click=tik_audio_download)
    row_tik = ft.Row(controls=[url_tiktok], alignment=ft.MainAxisAlignment.CENTER)
    row2_tik = ft.Row(controls=[btn1_tiktok, btn2_tiktok], alignment=ft.MainAxisAlignment.CENTER)
    #Facebook
    url_face = ft.TextField(label="Type The Facebook Video URL Here", width=800, border_color="blue")
    btn1_face = ft.FloatingActionButton(icon=ft.icons.VIDEO_LIBRARY, text="Download Video",bgcolor="blue", on_click=fb_download_video)
    btn2_face = ft.FloatingActionButton(icon=ft.icons.AUDIOTRACK, text="Download Audio", bgcolor="blue", on_click=fb_download_audio)
    row_face = ft.Row(controls=[url_face], alignment=ft.MainAxisAlignment.CENTER)
    row2_face = ft.Row(controls=[btn1_face, btn2_face], alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Row(controls=[down_progress], alignment=ft.MainAxisAlignment.CENTER)
    #groups
    container1 =ft.Container(content=ft.Column(controls=[row2,row3,row4]),padding=15)
    container2 =ft.Container(content=ft.Column(controls=[row_tik,row2_tik,row4]), padding=15)
    container3 =ft.Container(content=ft.Column(controls=[row_face,row2_face,row4]), padding=15)
    
    page.snack_bar = ft.SnackBar(ft.Text(f"Download Finished, Your File Is Ready", size=18, color="black", text_align=ft.TextAlign.CENTER), bgcolor=ft.colors.SECONDARY)
    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        indicator_color="red",
        tab_alignment=ft.TabAlignment.CENTER,
        #divider_color="black",
        indicator_border_radius=10,
        tabs=[
            ft.Tab(
                tab_content=ft.Icon(ft.icons.VIDEOCAM, color="red"),
                content=ft.Container(
                    content=container1,
                    alignment=ft.alignment.center,
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.TIKTOK, color="white"),
                content=ft.Container(container2,
                    alignment=ft.alignment.center,)
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.FACEBOOK, color="blue"),
                icon=ft.icons.SETTINGS,
                content=ft.Container(container3,
                    alignment=ft.alignment.center,)
            ),
        ],
        expand=1,  
    )
    
    await page.add_async(row1, t, row4)



ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)