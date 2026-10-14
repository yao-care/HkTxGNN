---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 5
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ivabradine：從心臟相關適應症到多毛症（Hypertrichosis）

## 一句話總結

Ivabradine 是一種降低心率的藥物，香港已有多張單方許可證，但本次資料中未收錄明確的核准適應症文字。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效（預測分數 99.79%），
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未收錄 |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未提供 MOA 欄位）。根據藥理學公認知識，Ivabradine 選擇性抑制竇房結中 HCN 通道所介導的心臟起搏電流 (If)，藉此降低心率。

多毛症是毛囊生長異常的疾病。HCN 通道抑制與毛髮生長調控之間，目前沒有已確立的關聯。一般與多毛症相關的藥物（如 minoxidil）是透過開啟鉀通道作用，機轉與 Ivabradine 不同，因此任何連結都只是推測。

TxGNN 的高分更可能來自知識圖譜中與毛髮相關節點的鄰近關係，而非生物學上的合理性。其他排名靠前的預測（Ambras 型先天性全身多毛症、伴有牙齒/牙周異常的畸形症候群、以 Dandy-Walker 畸形為主要特徵的症候群、孤立性遺傳性毛幹異常）同樣缺乏機轉依據與實證支持，多為先天性遺傳或發育異常，並非心率控制藥物可處理的目標。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 10 張有效的單方許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-55439 | CORALAN TAB 5MG | SERVIER HONG KONG LIMITED |
| HK-55438 | CORALAN TAB 7.5MG | SERVIER HONG KONG LIMITED |
| HK-68861 | IVABRADINE SANDOZ TABLETS 5MG | SANDOZ HONG KONG LIMITED |
| HK-68766 | BRAVIGO TABLETS 7.5MG | SB PHARMA LIMITED |
| HK-68233 | IVACORD 7.5 TABLETS 7.5MG | JACOBSON MARKETING LIMITED |

## 安全性考量

- **藥物交互作用**：本次共查得 100 筆交互作用，以下為部分列出的重大 (Major) 等級項目：
  - Aprepitant
  - Clarithromycin
  - Cisapride
  - Clotrimazole
  - Cobicistat
  - Dolasetron
  - Granisetron
  - Levofloxacin
  - Ondansetron
  - Palonosetron
  - Papaverine
- 中度 (Moderate) 等級的項目包括 Famotidine、Ranitidine、Cimetidine、Nizatidine、Dexamethasone、Miconazole 等。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的新適應症完全沒有臨床試驗或文獻支持，證據等級僅為 L5。
- Ivabradine 的作用機轉（抑制 HCN 通道降低心率）與毛髮生長或先天性發育異常之間，沒有可信的機轉連結。

**若要推進需要：**
- 補齊 Ivabradine 的作用機轉資料，並重新評估 HCN 通道與毛囊生物學之間是否存在任何關聯。
- 取得香港衛生署仿單中的警語、禁忌症與核准適應症文字，完成安全性篩選。
- 若仍要探索，需先有前臨床（細胞或動物毛囊模型）證據，再考慮臨床研究。
- 確認給藥途徑的可行性（目前僅有口服錠劑，資料中無外用劑型）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

