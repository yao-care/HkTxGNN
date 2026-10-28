---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 377
evidence_level: L5
indication_count: 6
monitor_inn: "FINASTERIDE"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
last_modified_at: 2026-10-28
description: "Finasteride：預測新適應症為Ambras type hypertrichosis universalis congenita（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Finasteride: Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## 一句話總結

Finasteride 在知識圖譜中記錄的原適應症為良性前列腺增生 (benign prostatic hyperplasia)。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有臨床試驗**，僅有 **4 篇間接相關的文獻**（皆為 1999–2003 年的敘述性或方法學文章），整體屬於低度證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Ambras type hypertrichosis universalis congenita |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

> 說明：predicted_indications 中排名第 2 的多毛症是唯一有文獻的預測。排名第 1 的 Ambras 型先天性全身多毛症分數略高，但完全沒有試驗或文獻，也缺乏機轉依據。本報告以有資料可評估的多毛症為主軸，並在下方附上其他預測的簡要比較。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，Finasteride 抑制第二型 5-α 還原酶，降低二氫睾酮 (DHT)，進而減少毛囊中的雄性素訊號。這是它在雄性禿（男性型落髮）中被使用的基礎。

不過，多毛症的定義是毛髮增生發生在**非雄性素依賴**的部位，與雄性素依賴的多毛 (hirsutism) 不同。因此 DHT 抑制的機轉連結偏弱，只可能出現在與 hirsutism 重疊的部分。

檢索到的 4 篇文獻都不是 Finasteride 治療多毛症的對照試驗，因此至多屬於間接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | 成人多毛症多為藥物誘發（如 minoxidil、cyclosporine）、代謝或腫瘤伴隨所致，與 hirsutism 的荷爾蒙評估不同 |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | 回顧雄性禿與 hirsutism 的新治療選項，著重口服療法 |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | 提到 Finasteride 用於男性型落髮，雷射除毛用於多毛症與 hirsutism |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | 方法學／診斷工具介紹 | Der Hautarzt | 介紹 TrichoScan 數位毛髮分析工具，並非 Finasteride 療效研究 |

## 香港上市資訊

下表僅列出 5 張代表性許可證（資料顯示至少 20 張，清單可能不完整）。所有許可證皆為單一成分製劑，目前資料未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 規格 | 製造商／持證商 |
|---------|------|------|-----------|
| HK-36604 | PROSCAR TAB 5MG | 5 毫克錠劑 | ORGANON HONG KONG LIMITED |
| HK-63379 | PROPECIA TABLET 1MG | 1 毫克錠劑 | ORGANON HONG KONG LIMITED |
| HK-58465 | FINASTERIDE-TEVA TAB 5MG | 5 毫克錠劑 | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-64019 | FINASTERIDE-TEVA TABLETS 1MG | 1 毫克錠劑 | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-66014 | HOVID FINASTERIDE TABLETS 1MG | 1 毫克錠劑 | HOVID LIMITED |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：肝臟疾病、膽囊疾病。
- **藥物交互作用**：資料庫查詢到 100 筆交互作用紀錄，目前列出的皆未標示嚴重度分級，例如 Calcitriol、Doxycycline、Bupropion、Metformin、Omeprazole、Morphine 等，臨床意義需另行查證。
- **生殖毒性考量**：預測資料指出 Finasteride 對男性胎兒生殖器發育有致畸風險，使用於發育相關疾病並不適當。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，4 篇文獻均為間接的敘述性或方法學文章，無直接研究顯示 Finasteride 對多毛症有效，因此證據等級為 L5。

**其他預測的簡述（均建議 Hold，證據等級 L5）：**
- Ambras 型先天性全身多毛症（0.9999）：由基因結構變異引起，非雄性素驅動，無試驗與文獻。
- 伴有牙齒／牙周異常的畸形症候群（0.9999）：無可辨識的機轉連結。
- 以 Dandy-Walker 畸形為主要特徵的症候群（0.9999）：結構性發育異常，且 Finasteride 有致畸疑慮。
- 單純遺傳性毛幹異常（0.9999）：多非雄性素介導，獲益可能性低。
- 家族性單純睫毛過長（0.9915）：屬罕見遺傳特徵，分數最低，無證據。

**若要推進需要：**
- 補充作用機轉資料（MOA）與香港仿單的警語、禁忌症。
- 針對 hirsutism 與多毛症做直接的文獻系統性檢索，區分雄性素依賴與非依賴型。
- 若機轉分析仍支持，再規劃小型探索性研究；在此之前不建議推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

