---
layout: default
title: Nilotinib
parent: 中證據等級 (L3-L4)
nav_order: 619
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Nilotinib：預測新適應症為隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans)（證據等級 L4）。原適應症：慢性骨髓性白血病（BCR-ABL1 陽性）"
---

# Nilotinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Nilotinib：從慢性骨髓性白血病到隆突性皮膚纖維肉瘤

## 一句話總結

Nilotinib 是一種酪胺酸激酶抑制劑，原本用於 BCR-ABL1 陽性的慢性骨髓性白血病。
TxGNN 模型預測它可能對**隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans, DFSP)** 有效，
目前僅有 **1 篇文獻**（綜述類型），**尚無臨床試驗登記**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性骨髓性白血病（BCR-ABL1 陽性） |
| 預測新適應症 | 隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma protuberans) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。以下機轉推論來自 nilotinib 的一般藥理知識，仍需對照 DrugBank 或原廠資料確認。

Nilotinib 除了抑制 BCR-ABL1 之外，也會抑制 PDGFR-α/β 與 KIT。隆突性皮膚纖維肉瘤主要由 COL1A1-PDGFB 融合基因驅動，此融合會持續產生 PDGFB，造成 PDGFR-β 的自分泌活化。因此從標靶層面來看，用 nilotinib 阻斷 PDGFR 訊號有合理的生物學基礎。

目前唯一的文獻 (PMID 29408302, 2018) 是討論小分子 PDGFR 抑制劑在腫瘤治療角色的綜述。它支持「抑制 PDGFR 可用於此類腫瘤」的機轉方向，但**並非 nilotinib 專屬的臨床證據**。TxGNN 分數雖高，但屬於計算預測，不能視為臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29408302](https://pubmed.ncbi.nlm.nih.gov/29408302/) | 2018 | Review | Pharmacological Research | 綜述小分子 PDGFR 抑制劑在腫瘤性疾病的治療角色；支持機轉方向，但非 nilotinib 專屬臨床證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56797 | TASIGNA CAP 200MG | — | — |
| HK-60833 | TASIGNA CAP 150MG | — | — |

兩張許可證均為單一成分製劑，持有者為 Novartis Pharmaceuticals (HK) Limited，狀態皆為有效。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項。知識圖譜顯示本藥與嗜中性白血球低下、血小板低下、貧血相關，需留意血球變化 |
| 監測項目 | CBC（含分類）、肝功能、血糖、電解質（鉀、鈣、磷）、心電圖（QT 間期） |

其餘項目（致吐性分級、處置防護）請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **知識圖譜標示的禁忌/需謹慎疾病**（非仿單內容，僅供參考）：
  - 心血管：高血壓、long QT 症候群（含家族性）、torsades de pointes
  - 肝膽胰：肝病、膽囊疾病、高膽紅素血症（含 Gilbert 症候群）、胰臟炎
  - 血液：血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血（含巨球性貧血）
  - 代謝：高血糖、糖尿病、糖尿病酮酸中毒、低鉀、高鈣血症、腎鈣質沉著症、磷代謝異常、低磷血症

- **藥物交互作用**（共查得 100 筆，以下為部分重點）：
  - **重度 (Major)**：Dexamethasone、Clarithromycin、Picosulfuric acid、Polyethylene glycol（含電解質）
  - **中度 (Moderate)**：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole（制酸劑/PPI 類）；Hydrocortisone、Triamcinolone、Betamethasone、Budesonide（類固醇類）；Pioglitazone、Saxagliptin、Loperamide、Bupropion、Aprepitant、Bisacodyl

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高（99.31%），且 PDGFR 抑制的機轉推論合理，但目前只有一篇非 nilotinib 專屬的綜述，沒有臨床試驗，證據僅達 L4。
- 仿單的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 補充 nilotinib 在 DFSP 的直接臨床證據（臨床試驗、病例報告或回溯性研究）
- 從 DrugBank 取得正式的作用機轉資料，驗證 PDGFR 抑制的機轉推論
- 取得香港衛生署的仿單，補齊警語與禁忌症，並評估 QT 延長、肝毒性與藥物交互作用風險
- 確認香港許可證核准適應症與劑型資訊（目前為空白）
- 與現有 DFSP 標準治療（如其他 PDGFR 抑制劑）比較，評估 nilotinib 的相對價值
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

