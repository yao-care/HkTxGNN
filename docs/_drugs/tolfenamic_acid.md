---
layout: default
title: Tolfenamic Acid
parent: 僅模型預測 (L5)
nav_order: 887
evidence_level: L5
indication_count: 9
monitor_inn: "TOLFENAMIC ACID"
predicted_indications: ["headache disorder", "tendinitis", "rheumatoid arthritis", "trigeminal autonomic cephalalgia", "idiopathic granulomatous myositis", "myositis fibrosa", "fibromyalgia", "exostosis", "inclusion body myositis"]
last_modified_at: 2026-10-23
description: "Tolfenamic Acid：預測新適應症為頭痛疾患 (Headache Disorder)（證據等級 L5）。原適應症：許可證未載明"
---

# Tolfenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Tolfenamic Acid：從（許可證未載明原適應症）到頭痛疾患
{: .text-alpha }

## 一句話總結

Tolfenamic acid（甲滅酸類，fenamate 類非類固醇消炎藥）在香港的許可證資料中未載明核准適應症。
TxGNN 模型預測它可能對**頭痛疾患 (Headache Disorder)** 有效，目前資料中**沒有臨床試驗登記**，但有 **19 篇文獻**，其中多篇為偏頭痛的隨機對照試驗，直接支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 頭痛疾患 (Headache Disorder) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5（見下方說明） |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** 文獻中有數項針對偏頭痛（頭痛疾患的主要類型）的雙盲隨機對照試驗（如 PMID 6394143、2375249、3727918），但資料中沒有已登記並完成的 Phase 3 試驗，也未標示試驗階段。因此 L1 的認定主要依文獻分類，而非試驗登記，這點需在解讀時留意。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載。根據文獻，tolfenamic acid 是強效的前列腺素合成抑制劑（抑制環氧合酶），也有研究指出它可能影響白三烯路徑。

前列腺素會使痛覺受器敏感化，並參與神經性發炎、血管擴張和血小板聚集，這些都與偏頭痛發作有關。因此抑制前列腺素合成，在機轉上符合偏頭痛的急性與預防性治療。文獻也提到它與咖啡因、metoclopramide 合併使用，可處理發作時胃排空延遲、藥物吸收變差的問題。

此外，另有資料顯示 tolfenamic acid 為鎂氧化還原酶類 AKR1C3 的藥理標靶，但該資料屬藥理學交互作用，與頭痛適應症的關聯尚不明確。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6394143](https://pubmed.ncbi.nlm.nih.gov/6394143/) | 1984 | RCT | Cephalalgia | 比較 tolfenamic acid、metoclopramide、咖啡因及其組合治療偏頭痛發作 |
| [2375249](https://pubmed.ncbi.nlm.nih.gov/2375249/) | 1990 | RCT | Acta Neurol Scand | 雙盲交叉試驗，tolfenamic acid 對比 paracetamol 治療無預兆偏頭痛 |
| [3727918](https://pubmed.ncbi.nlm.nih.gov/3727918/) | 1986 | RCT | Acta Neurol Scand | 預防偏頭痛：tolfenamic acid 與 propranolol 均顯著優於安慰劑，降低發作次數與持續時間 |
| [7816790](https://pubmed.ncbi.nlm.nih.gov/7816790/) | 1994 | Review | Pharmacol Toxicol | 回顧 tolfenamic acid 於偏頭痛急性與預防治療的角色 |
| [7816789](https://pubmed.ncbi.nlm.nih.gov/7816789/) | 1994 | Review | Pharmacol Toxicol | 探討偏頭痛與前列腺素、白三烯的關係 |
| [9563211](https://pubmed.ncbi.nlm.nih.gov/9563211/) | 1998 | 隨機對照 | Headache | 速釋型 tolfenamic acid 與 sumatriptan 急性治療偏頭痛效果相當 |
| [12474702](https://pubmed.ncbi.nlm.nih.gov/12474702/) | 2002 | 隨機雙盲 | Medicina (Kaunas) | 192 位患者，tolfenamic acid 300 mg 與 pizotifen 比較預防偏頭痛 |
| [7976233](https://pubmed.ncbi.nlm.nih.gov/7976233/) | 1994 | 隨機雙盲交叉 | Acta Neurol Scand | 76 位患者，tolfenamic acid 與 propranolol 預防偏頭痛比較 |
| [89390](https://pubmed.ncbi.nlm.nih.gov/89390/) | 1979 | 雙盲交叉 | Lancet | 與 ergotamine 同等有效，噁心等副作用較少 |
| [10234467](https://pubmed.ncbi.nlm.nih.gov/10234467/) | 1999 | 回溯研究 | Cephalalgia | 與 sumatriptan 併用可降低偏頭痛復發 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50767 | TOLFEDINE TAB 20MG (VET) | 未載明 | 未載明 |

此許可證為單一成分製劑，品名標示為獸醫用（VET），因此不應視為人用偏頭痛或其他人類適應症的核准依據。

## 安全性考量

- **藥物交互作用：** 資料中僅有一筆藥理關聯，標靶為 AKR1C3，屬藥理資料，未標示臨床交互作用等級。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 偏頭痛有多項隨機對照試驗，顯示 tolfenamic acid 在急性與預防治療上有療效，且機轉（抑制前列腺素）合理。
- 但資料中沒有臨床試驗登記，香港許可證僅為獸醫用產品且未載明適應症，也缺乏警語與禁忌症資料，因此需設置保護措施。

**若要推進需要：**
- 取得香港衛生署人用產品的仿單，確認警語、禁忌症與核准適應症
- 補充作用機轉資料，並確認 AKR1C3 的臨床意義
- 評估近期（較新）的臨床證據，因現有文獻多為 1980–2000 年代研究
- 釐清人用劑型與給藥途徑的可及性
- 確認香港獸醫用產品與人用藥品的監管區別

**其他預測適應症（供參考）：**
- **類風濕性關節炎**（分數 0.9970）：有多項 RCT 與臨床研究（如 PMID 373084、373085），機轉上與抑制滑膜前列腺素生成一致，值得另行評估。
- **肌腱炎、三叉自律神經性頭痛、肉芽腫性肌炎、纖維性肌炎、纖維肌痛症、骨疣、包涵體肌炎**：僅有模型預測，無直接研究，證據等級 L5，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

