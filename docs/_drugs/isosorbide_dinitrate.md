---
layout: default
title: Isosorbide Dinitrate
parent: 僅模型預測 (L5)
nav_order: 417
evidence_level: L5
indication_count: 5
---

# Isosorbide Dinitrate
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

# Isosorbide Dinitrate：從心絞痛到肺動脈高壓（研究假說階段）

## 一句話總結

Isosorbide Dinitrate（ISDN）是傳統的有機硝酸酯類血管擴張劑，藥理上用於心絞痛與心臟衰竭。TxGNN 模型針對此藥產生 5 個新適應症預測，其中僅**肺動脈高壓 (Pulmonary Hypertension)** 有實質文獻佐證——**20 篇 PubMed 文獻**橫跨 1979–2025 年，機轉與 ISDN 的 NO 供體/血管擴張作用高度吻合；其餘落髮相關預測（雄性禿、先天性稀毛症等）雖 TxGNN 分數更高，卻完全查無臨床試驗或文獻，機轉上也與其病理（自體免疫、基因突變）無關，判斷為模型假陽性。

> 註：Evidence Pack 未提供 ISDN 的正式原適應症登記文字與 MOA 資料（原廠仿單/DrugBank 查詢均標記為缺口，見下方安全性考量），本報告的「原適應症」為該藥類別公開已知的臨床用途，非取自本 Evidence Pack 的許可證資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心絞痛／心臟衰竭（有機硝酸酯類；Evidence Pack 無許可證資料佐證） |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.98%（模型排名 733） |
| 證據等級 | L3（觀察性/血液動力學臨床研究，含 1 篇 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

ISDN 屬於 NO 供體，經 guanylate cyclase–cGMP 路徑誘發血管平滑肌鬆弛，達到全身及局部血管擴張效果。這是其治療心絞痛/心臟衰竭的核心機轉，也是預測邏輯的出發點。

肺血管床對 NO–cGMP 路徑高度敏感，理論上 ISDN 可降低平均肺動脈壓（mPAP）並減輕右心後負荷。這條機轉關聯已有近 45 年（1979–2025）持續的人體血液動力學研究支持，涵蓋 COPD 相關 PH、間質性肺纖維化相關 PH、原發性 PH 及心因性 PH 等多種次族群，一致觀察到急性肺血管阻力/壓力下降。

相對地，同一批預測中分數更高的「落髮」相關適應症（alopecia、congenital hypotrichosis milia、hypotrichosis simplex of the scalp、diffuse alopecia areata）查詢臨床試驗、ICTRP、文獻資料庫皆為 0 筆結果，且其自身的機轉推論也承認「病理與血管擴張無直接關聯」，屬於模型內插但缺乏實證支持的高分候選，建議暫不推進。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 與 ICTRP 皆為 0 筆）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19620510](https://pubmed.ncbi.nlm.nih.gov/19620510/) | 2009 | RCT | Hypertension | 固定劑量 ISDN/hydralazine 改善高血壓誘發舒張性心衰竭之心肌重塑 |
| [373940](https://pubmed.ncbi.nlm.nih.gov/373940/) | 1979 | 隨機雙盲對照 | Clin Pharmacol Ther | 口服 ISDN 在 COPD 合併肺高壓患者中降低肺動脈壓 |
| [39164577](https://pubmed.ncbi.nlm.nih.gov/39164577/) | 2025 | 臨床研究 | Heart and Vessels | Bolus ISDN 在合併心肺共病之肺高壓患者中降低 mPAP，且不明顯減少心輸出量 |
| [3409916](https://pubmed.ncbi.nlm.nih.gov/3409916/) | 1988 | 臨床研究（2年追蹤） | European Heart Journal | ISDN 長期治療使間質性肺纖維化患者的肺高壓獲得持續性血液動力學改善 |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | 臨床研究 | Bull Eur Physiopathol Respir | 舌下 ISDN 顯著降低 COPD 患者肺動脈壓與右心作功 |
| [8908227](https://pubmed.ncbi.nlm.nih.gov/8908227/) | 1996 | 臨床研究 | Acta Anaesthesiol Scand | ISDN 對末期心肌病患者肺血管的選擇性優於 NTG |
| [7125407](https://pubmed.ncbi.nlm.nih.gov/7125407/) | 1982 | 臨床研究 | Annals of Internal Medicine | 舌下 isoproterenol 合併 ISDN 為少數能顯著降低原發性肺高壓肺血管阻力的組合 |
| [28810603](https://pubmed.ncbi.nlm.nih.gov/28810603/) | 2017 | 動物實驗 | Exp Ther Med | 氣管內給予 ISDN 改善心肌梗塞後心衰竭大鼠之肺動脈壓與心室重塑 |
| [39398794](https://pubmed.ncbi.nlm.nih.gov/39398794/) | 2024 | 世代研究 | Cureus | 洗腎患者肺高壓負擔評估及治療策略回顧（提供疾病族群背景） |
| [3348140](https://pubmed.ncbi.nlm.nih.gov/3348140/) | 1988 | 臨床研究 | Am J Cardiol | 開心手術中靜脈注射 ISDN 顯著改善右側心衰竭之肺血管阻力 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> Evidence Pack 標記此藥的 TFDA/香港仿單警語與禁忌症資料為**阻斷性缺口（DG001，Blocking）**——在補齊前無法進入安全性初評（S1）。DDI 查詢亦無結果（`query_status: not_found`）。此為推進本適應症前的首要待辦事項。

---

## 結論與下一步

**決策：Hold**

**理由：**
肺動脈高壓的機轉關聯性明確，且有近 45 年、跨多種病因次族群一致的人體血液動力學證據支持（L3），是本次五個預測中唯一具實證基礎者。但香港未上市（0 張許可證）、且仿單警語/禁忌症資料存在阻斷性缺口（DG001），現有文獻也多為急性血液動力學觀察而非長期療效與安全性 RCT，尚不足以支持進入臨床決策階段。

**若要推進需要：**
- 取得 ISDN 完整仿單/處方資訊，補齊警語、禁忌症、DDI（DG001，Blocking，最優先）
- 補充正式 MOA 佐證文件（DG002，查詢 DrugBank API）
- 針對肺動脈高壓設計前瞻性隨機對照試驗，驗證長期療效與安全性（現有證據多為急性反應）
- 確認香港上市/許可證申請路徑
- 落髮相關預測（alopecia 系列）證據不足、機轉不合理，建議列為低優先或排除
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

