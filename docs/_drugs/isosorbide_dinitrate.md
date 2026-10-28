---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 489
evidence_level: L5
indication_count: 10
monitor_inn: "ISOSORBIDE DINITRATE"
predicted_indications: ["alopecia", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "pulmonary hypertension", "diffuse alopecia areata", "vascular disease", "hypertrichosis (disease)", "kyphoscoliotic heart disease", "visceral calciphylaxis", "arterial thoracic outlet syndrome"]
last_modified_at: 2026-10-23
description: "Isosorbide Dinitrate：預測新適應症為Alopecia（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Isosorbide Dinitrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Isosorbide Dinitrate: Alopecia
{: .text-alpha }

## 一句話總結

二硝酸異山梨醇酯是一種硝酸酯類血管擴張劑，香港共有 5 張有效單方許可證，但許可證資料中未載明核准適應症文字。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，目前有 **0 個臨床試驗**和 **19 篇相關文獻**（多為小型血行動力學研究），證據等級為 L5。

> 說明：預測排名第 1 的是禿髮 (alopecia)，但該預測完全沒有臨床或文獻證據。本報告以有文獻資料的肺動脈高壓為主要評估對象，並在後文簡述其他預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Alopecia |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

**證據等級說明：** 資料中雖有肺動脈高壓的血行動力學研究，但多數為 1979–1996 年的小型短期研究，且缺少已登記的臨床試驗。資料編制時的自動評分給予 L3。依本報告的判定規則，L1–L4 須有直接研究該疾病的試驗或文獻；本案文獻雖直接涉及肺動脈高壓，但缺乏完整摘要與結果數據可供確認，保守判定為 L5，並列為研究假說。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，二硝酸異山梨醇酯屬於硝酸酯類藥物，一般認為可作為一氧化氮 (NO) 供體，造成靜脈與肺動脈血管擴張，降低前負荷與肺血管阻力。

肺動脈高壓的核心問題是肺血管阻力升高，因此在機轉上，血管擴張劑有其合理性。相關文獻顯示，此藥在慢性阻塞性肺病 (COPD) 合併肺高壓、末期心肌病變與間質性肺纖維化病人中，可降低肺動脈壓。

但需注意限制：
- 急性血行動力學改善不等於長期臨床獲益。
- 在 COPD 患者中，可能因通氣灌注失配而抵消效益。
- 2025 年的研究指出，此藥在前微血管型肺高壓可能降低心輸出量與血壓。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | 隨機雙盲臨床血行動力學研究 | Clin Pharmacol Ther | COPD 合併肺高壓患者（18 人）口服此藥對比安慰劑，評估血行動力學反應 |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | 臨床血行動力學研究 | Bull Eur Physiopathol Respir | COPD 患者（各 27 人）舌下給藥，肺動脈壓與心輸出量下降；硝酸甘油可降低肺血管阻力，此藥則否 |
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | 臨床研究 | Heart Vessels | 靜脈單次注射用於合併心肺疾病的肺高壓，探討平均肺動脈壓與血壓下降程度 |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | 臨床血行動力學研究 | Acta Anaesthesiol Scand | 末期心肌病變患者的肺血管反應，比較此藥與硝酸甘油 |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | 臨床研究 | Eur Heart J | 18 位間質性肺纖維化患者，急性給藥使肺血管阻力下降，兩年治療在部分患者維持血行動力學改善 |
| [7125407](https://pubmed.ncbi.nlm.nih.gov/7125407/) | 1982 | 臨床研究 | Ann Intern Med | 10 位原發性肺高壓女性；此藥是唯一能降低肺動脈壓的非注射藥物 |
| [2868878](https://pubmed.ncbi.nlm.nih.gov/2868878/) | 1986 | 回顧 | Drugs | 原發性肺高壓藥物治療回顧，指出尚缺乏足夠的臨床試驗 |
| [6530750](https://pubmed.ncbi.nlm.nih.gov/6530750/) | 1984 | 病例報告 | Jpn Heart J | 一位原發性肺高壓患者以 prazosin 合併此藥治療，肺血管阻力持續下降 |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | 動物研究 | Exp Ther Med | 大鼠心衰模型氣管內給藥可改善肺動脈壓與心室重塑 |
| [2498122](https://pubmed.ncbi.nlm.nih.gov/2498122/) | 1989 | 動物研究 | Exp Mol Pathol | 與其他藥物比較對野百合鹼誘發肺高壓的影響 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68629 | APT-ISOSORBIDE DINITRATE TABLETS 10MG | 未載明 | 未載明 |
| HK-40553 | APO-ISDN SUBLINGUAL TAB 5MG | 未載明 | 未載明 |
| HK-36369 | APO-ISDN TAB 10MG | 未載明 | 未載明 |
| HK-44851 | ISORDE PLUS TAB 10MG | 未載明 | 未載明 |
| HK-68203 | SOLBID TABLETS 10MG | 未載明 | 未載明 |

以上 5 張均為有效的單方許可證。

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：低血壓、肥厚性心肌病變、冠狀動脈疾病、中風與腦血管疾病、心肌梗塞、血紅素病變與貧血、甲狀腺機能亢進（含葛瑞夫茲氏病）、顱內高壓與腦出血等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Bupropion、Morphine、Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin、Rosiglitazone、Dronabinol、Nabilone、Opium、Sapropterin
  - 輕度：Omeprazole

其餘警語與禁忌症請參考原廠仿單。

---

## 其他預測適應症簡述

| 預測疾病 | 分數 | 證據 |
|---------|------|------|
| 禿髮 (alopecia) | 0.9999 | 無，機轉屬推測 |
| 先天性稀毛症合併粟丘疹 | 0.9999 | 無，缺乏合理機轉 |
| 頭皮單純性稀毛症 | 0.9999 | 無，缺乏合理機轉 |
| 瀰漫性斑禿 | 0.9998 | 無，缺乏免疫機轉關聯 |
| 血管疾病 | 0.9997 | 僅有間接研究；唯一直接相關的是糖尿病足潰瘍噴劑的 Phase 3 試驗（NCT02789033，68 人，結果未提供），且該疾病範疇過廣，並與既有用途重疊 |
| 多毛症、脊柱後側彎心臟病、內臟鈣化防禦、動脈型胸廓出口症候群 | 99.95–0.9997 | 無 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 肺動脈高壓在機轉上合理，但現有文獻多為數十年前的小型短期血行動力學研究，缺少登記的臨床試驗與長期結局資料，且在部分族群有降低心輸出量與血壓的風險。
- 其他預測（尤其毛髮相關疾病）完全沒有證據支持。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 補充詳細作用機轉資料
- 針對肺高壓分型（前微血管型 vs. 後微血管型）進行系統性文獻回顧
- 設計小型前瞻性研究，評估血行動力學與長期臨床結局
- 進一步確認糖尿病足潰瘍 Phase 3 試驗（NCT02789033）的結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

