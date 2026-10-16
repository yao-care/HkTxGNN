---
layout: default
title: Minocycline
parent: 僅模型預測 (L5)
nav_order: 589
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Minocycline：預測新適應症為點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L5）。原適應症：泌尿道感染、支氣管炎、痤瘡、牙周炎、淋病等"
---

# Minocycline
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

# Minocycline：從細菌感染（泌尿道感染、痤瘡等）到點狀上皮角膜結膜炎

## 一句話總結

Minocycline 是四環素類抗生素，原本用於泌尿道感染、支氣管炎、痤瘡、牙周炎、淋病等多種感染性疾病。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染、支氣管炎、痤瘡、牙周炎、淋病等（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Minocycline 屬於四環素類抗生素，其在細菌感染中的療效已被證實。

依一般藥理背景知識（並非來自本次彙整的資料，也未經驗證），minocycline 具有抗發炎與抑制基質金屬蛋白酶（MMP）的特性，同類藥物如 doxycycline 也用於瞼板腺功能異常與眼瞼炎等眼表疾病。這些特性在機轉上可能與眼表發炎有關。

不過這僅是**假設性的推論**，不能視為對點狀上皮角膜結膜炎有效的證據。另一個預測適應症為暴露性角膜炎（TxGNN 分數 99.20%），同樣沒有任何臨床證據；該病主要靠恢復眼表保護與潤滑處理，minocycline 的角色僅屬推測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40746 | APO-MINOCYCLINE CAP 100MG | 膠囊（品名標示） | 未提供 |
| HK-40747 | APO-MINOCYCLINE CAP 50MG | 膠囊（品名標示） | 未提供 |

兩張許可證皆為單方、有效，持證商為 HIND WING CO LTD。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯，非仿單文字）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、困難梭狀芽孢桿菌結腸炎、周產期壞死性腸炎、假性腦瘤、顱內高壓、食道運動障礙。
- **藥物交互作用**：共查得 100 筆，以下為已列出的部分重點：
  - **嚴重 (Major)**：Isotretinoin、Acitretin（維生素 A 類藥物併用，須特別避免）
  - **中度 (Moderate)**：Ethinylestradiol、Amoxicillin、Ampicillin、Aminolevulinic acid（外用）、Sodium citrate、Balsalazide、Bismuth subcitrate potassium、Calcium phosphate、Calcium acetate、Brentuximab vedotin、Cannabidiol、Asparaginase 類等
  - **輕微 (Minor)**：Acetazolamide、Hydrochlorothiazide、Amiloride、Bumetanide

香港仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測分數（99.63%），沒有臨床試驗或文獻佐證，證據等級為 L5。
- 作用機轉資料與香港仿單安全性資料均缺漏，無法進行安全性初篩。

**若要推進需要：**
- 補齊 minocycline 的作用機轉資料（如 DrugBank）
- 下載並解析香港衛生署仿單，取得警語與禁忌資訊
- 系統性檢索眼表疾病（點狀上皮角膜結膜炎）相關的臨床與前臨床文獻
- 評估給藥途徑的可行性（目前香港僅有口服膠囊，眼科用途所需劑型尚未確認）
- 確認路徑相容性與新適應症的安全性風險（如眼部局部給藥 vs. 全身給藥）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

