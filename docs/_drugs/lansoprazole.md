---
layout: default
title: Lansoprazole
parent: 僅模型預測 (L5)
nav_order: 509
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Lansoprazole：預測新適應症為十二指腸胃逆流 (Duodenogastric Reflux)（證據等級 L5）。原適應症：胃潰瘍、消化性潰瘍、胃食道逆流症、食道炎、十二指腸潰瘍、Zollinger-Ellison 症候群"
monitor_inn: "LANSOPRAZOLE"
predicted_indications: ["duodenal obstruction"]
---

# Lansoprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Lansoprazole：從胃潰瘍／胃食道逆流到十二指腸胃逆流

## 一句話總結

Lansoprazole 是質子幫浦抑制劑（PPI），原本用於胃潰瘍、十二指腸潰瘍、胃食道逆流症、食道炎及 Zollinger-Ellison 症候群等胃酸相關疾病。
TxGNN 模型預測它可能對**十二指腸胃逆流 (Duodenogastric Reflux)** 有效，但目前**沒有相關臨床試驗**，僅有 **1 篇**一般性的 PPI 臨床使用回顧文獻，屬於模型預測階段的研究假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃潰瘍、消化性潰瘍、胃食道逆流症、食道炎、十二指腸潰瘍、Zollinger-Ellison 症候群（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 十二指腸胃逆流 (Duodenogastric Reflux) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L5（僅有模型預測，無針對此適應症的實際研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載。依一般藥理知識，Lansoprazole 是質子幫浦抑制劑，不可逆地抑制胃壁細胞的 H+/K+ ATP 酶，降低胃酸分泌。

十二指腸胃逆流是指十二指腸內容物（含膽汁與胰液）逆流入胃。當胃酸是黏膜傷害的共同因子時，降低胃酸可能減輕黏膜損傷與症狀。這與其已核准的胃酸相關疾病（胃食道逆流症、食道炎、胃及十二指腸潰瘍）有部分重疊。

不過，PPI 並不作用於膽汁逆流本身，也不改善幽門或十二指腸的蠕動，因此兩者的關聯是**間接且僅限於症狀緩解**。0.997 的高分很可能來自知識圖譜中與已核准上消化道適應症的網路鄰近性，**不等於臨床驗證**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | Eur J Clin Pharmacol | PPI 臨床使用與藥動學回顧，涵蓋消化性潰瘍、幽門螺旋桿菌感染、胃食道逆流症、NSAID 相關胃腸損傷及 Zollinger-Ellison 症候群；內容並非針對十二指腸胃逆流 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51917 | TAKEPRON OD TAB 30MG (ENTERIC C. MICROGRANULES) | 口崩錠 | 未提供 |
| HK-51919 | TAKEPRON OD TAB 15MG (ENTERIC C. MICROGRANULES) | 口崩錠 | 未提供 |
| HK-65437 | LANPO GASTRO-RESISTANT CAPSULES 15MG | 耐胃酸膠囊 | 未提供 |
| HK-65436 | LINX GASTRO-RESISTANT CAPSULES 15MG | 耐胃酸膠囊 | 未提供 |
| HK-59079 | LANPIRA TAB 30MG | 錠劑 | 未提供 |

（共 9 張有效許可證，皆為單一成分製劑，無已註銷者；此處僅列出 5 張。）

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分重點：
  - **Major（嚴重）**：Acalabrutinib、Atazanavir
  - **Moderate（中度）**：Hydrochlorothiazide、Amphotericin B、Amikacin、Atorvastatin、Fenofibrate、Apalutamide、Aprepitant、Bosutinib、Brigatinib、Bromocriptine 等
  - **Minor（輕微）**：Acetylsalicylic acid、Axitinib、Brivaracetam、Cyanocobalamin 等
- **知識圖譜標示的疾病關聯警示**（來自藥物－疾病關係資料，非仿單文字）：包括長 QT 症候群／尖端扭轉型心室頻脈、肝衰竭與肝病、腎臟疾病、紫質症、骨質疏鬆、心肌梗塞與腦中風、貧血、困難梭狀芽孢桿菌結腸炎、重症肌無力等。這些需與仿單核對後才能作為臨床判讀依據。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但缺乏針對十二指腸胃逆流的臨床試驗，唯一文獻也只是一般性的 PPI 回顧。
- 機轉上 PPI 無法處理膽汁逆流的根本原因，僅可能緩解酸相關症狀，屬間接效益。

**若要推進需要：**
- 針對十二指腸胃逆流（含膽汁逆流）使用 PPI 的專門文獻搜尋與系統性回顧
- 補齊 Lansoprazole 的作用機轉資料（DrugBank）
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 若有探索價值，先設計小型探索性臨床研究，以症狀改善及膽汁逆流指標為終點
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

