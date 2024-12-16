# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:29:23 2024

@author: Admin
"""

import pyodbc

def get_connection():
    conn=pyodbc.connect('DRIVER={SQL SERVER};'
                        'SERVER=PC4\SQLEXPRESS'
                        'DATABASE=CepTelefonuTamir;'
                        'UID=sa;'
                        'PWD=your_password')
    return conn
def müşteri_ekle(ad,soyad,telefon_no,email,adres):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("EXEC MüşetiEkle ?,?,?,?,?",
                   (ad,soyad,telefon_no,email,adres))
    conn.commit()
    print("Müşteri başarıyla eklendi!")
    conn.close()
    
def telefon_ekle(müşteri_ıd,marka,model,seri_no,durum):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("EXEC TelefonEkle ?,?,?,?,?",
                   (müşteri_ıd,marka,model,seri_no,durum))
    conn.commit()
    print("Telefon başarıyla eklendi")
    conn.close()
    
def tamir_kaydı_ekle(telefon_id,çalışan_id,tamir_tarihi,teslim_tarihi,açıklama,maliyet):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("EXEC TamirKaydıEkle ?,?,?,?,?,?",(telefon_id,çalışan_id,tamir_tarihi,teslim_tarihi,açıklama,maliyet))
    conn.commit()
    print("Tamir kaydı başarıyla oluşturuldu!")
    conn.close()
    
def müşteri_ve_telefon_listele():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("EXEC MüşteriVeTelefonListele")
    rows =cursor.fetchall()
    for row in rows:
        print(f"Müşteri:{row.Ad}{row.soyad},Telefon:{row.Marka}{row.Model},Seri No:{row.SeriNo},Durum:{row.Durum}")
    conn.close()
    
def main():
    while True:
        print("\n1.Müşyteri Ekle")
        print("2.Telefon Ekle")
        print("3. Tamir Kaydı Ekle")
        print("4.Müşteri Ve Telefon Listele")
        print("5.çıkış")
        
        secim=input("SEçiminizi Yapın: ")
        
        if seçim=="1":
            ad=input("Ad: ")
            soyad=input("Soyad: ")
            telefon_no=input("Telefon No: ")
            email=input("Email: ")
            adres=input("Adres: ")
            müşteri_ekle(ad,soyad,telefon_no,email,adres)
        elif secim=="2":
            müşteri_id=int(input("Müşteri ID: "))
            marka=input("Marka: ")
            model=input("Model: ")
            seri_no=input("Seri No:" )
            durum=input("Durum: ")
            telefon_ekle(müşteri_ıd,marka,model,seri_no,durum)
        elif secim=="3":
            telefon_id=int(input("Telefon ID: "))
            çalışan_id=int(input(("Çalışan ID: "))
            tamir_tarihi=(input("Tamir Tarihi(YYYY-MM-DD):")
            teslim_tarihi=input("Teslim Tarihi(YYYY-MM-DD):")
            açıkalama= input("Açıklama: ")
            maliyet=input("Maliyet: ")
           tamir_kaydı_ekle (telefon_id,çalışan_id,tamir_tarihi,teslim_tarihi,açıkalama,maliyet)
        elif secim=="4":
            müsteri_ve_telefon_listele()
        elif secim=="5":
            print("Çıkılıyor....")
            break
        else:
            print("Geçersizz seçim,tekrar deneyin.")
            
if__name__--"__main__":
    main()            
            


            