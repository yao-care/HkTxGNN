---
layout: default
title: Ethanol
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 2
---

# Ethanol
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

# Ethanol：從外用消毒製劑成分到偏頭痛（模型預測，不建議推進）

## 一句話總結

Ethanol（乙醇）在香港登記的產品多為外用消毒溶液，也用作注射劑的溶媒成分。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，但目前**沒有任何臨床試驗以乙醇治療偏頭痛**。
相關文獻幾乎都把乙醇當作偏頭痛的**誘發因子**，方向與治療相反。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.29% |
| 證據等級 | L5（僅有模型預測，無支持治療用途的實際研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

原適應症欄位：香港許可證資料中沒有核准適應症文字，因此未列出。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ethanol 是外用消毒溶液及部分製劑溶媒的成分，這些用途都與偏頭痛無關。

**這個預測缺乏合理的治療機轉支持。** 現有文獻一致指出，酒精是偏頭痛的誘發因子，而非治療手段。
- 前臨床研究顯示，乙醇的代謝物乙醛（acetaldehyde）會經由 CGRP 受體與 Schwann 細胞的 TRPA1，在小鼠身上引發眼眶周圍機械性異痛（PMID 37101198）。這與治療方向相反。
- 基因研究（如 ADH2 基因型）探討的是乙醇代謝與偏頭痛風險的關聯，不是療效。

TxGNN 的高分較可能反映乙醇與偏頭痛在文獻中頻繁共現（誘發因子、共病、基因），而非治療關係。
第二個預測適應症「伴腦幹先兆的偏頭痛 (Migraine with brainstem aura)」（分數 99.14%）同樣沒有臨床試驗，也沒有乙醇特異的治療證據。

## 臨床試驗證據

以下列出檢索到的 10 個偏頭痛相關試驗。**這些試驗全都不是以乙醇治療偏頭痛**，僅供參考。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05175521](https://clinicaltrials.gov/study/NCT05175521) | 不適用 | 進行中（不再招募） | 50 | 吸入異丙醇（isopropyl alcohol）蒸氣對比尤加利氣味，用於急性偏頭痛噁心。這是異丙醇，不是乙醇 |
| [NCT07301008](https://clinicaltrials.gov/study/NCT07301008) | Phase 4 | 招募中 | 60 | Rimegepant 用於可預測誘發因子（包含少量飲酒）引起的偏頭痛。酒精在此是誘因 |
| [NCT06197542](https://clinicaltrials.gov/study/NCT06197542) | 不適用 | 完成 | 54 | 主動釋放技術與器械輔助軟組織鬆動，用於偏頭痛觸發點 |
| [NCT03238781](https://clinicaltrials.gov/study/NCT03238781) | Phase 2 | 完成 | 343 | AMG 301 對比安慰劑，用於預防偏頭痛 |
| [NCT00109083](https://clinicaltrials.gov/study/NCT00109083) | Phase 2 | 完成 | 300 | 研究藥物 RWJ-333369 用於預防偏頭痛的劑量範圍試驗 |
| [NCT04017741](https://clinicaltrials.gov/study/NCT04017741) | Phase 4 | 完成 | 8 | 枕大神經阻斷（局部麻醉劑加類固醇）用於慢性偏頭痛 |
| [NCT05454826](https://clinicaltrials.gov/study/NCT05454826) | 不適用 | 完成 | 26 | 放鬆運動加冷敷用於偏頭痛 |
| [NCT02169830](https://clinicaltrials.gov/study/NCT02169830) | 不適用 | 終止 | 35 | Nortriptyline 與 topiramate 交叉試驗，用於前庭性偏頭痛 |
| [NCT05685225](https://clinicaltrials.gov/study/NCT05685225) | Phase 2 | 撤回 | 0 | Naltrexone/acetaminophen 複方用於急性偏頭痛 |
| [NCT07254598](https://clinicaltrials.gov/study/NCT07254598) | 不適用 | 尚未招募 | 84 | 眼外肌肌張力技術輔助手法治療，用於無先兆偏頭痛 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37612595](https://pubmed.ncbi.nlm.nih.gov/37612595/) | 2023 | 系統性回顧與統合分析 | J Headache Pain | 評估原發性頭痛患者的酒精攝取與關聯性；摘要顯示既有文獻結論不一致，但偏頭痛患者多避免飲酒 |
| [36373782](https://pubmed.ncbi.nlm.nih.gov/36373782/) | 2022 | Review | Headache | 探討酒精與偏頭痛之間的複雜關係（無摘要） |
| [18231712](https://pubmed.ncbi.nlm.nih.gov/18231712/) | 2008 | Review | J Headache Pain | 約三分之一偏頭痛患者曾把酒精視為誘因，但僅約 10% 稱其為經常誘因 |
| [41305669](https://pubmed.ncbi.nlm.nih.gov/41305669/) | 2025 | Review | Nutrients | 酒精與頭痛相關，但確切致病機轉仍不明 |
| [23614946](https://pubmed.ncbi.nlm.nih.gov/23614946/) | 2013 | 觀察性（誘因調查） | Pain Med | 調查酒精飲品作為原發性頭痛誘因的角色 |
| [37101198](https://pubmed.ncbi.nlm.nih.gov/37101198/) | 2023 | 前臨床 | J Biomed Sci | 乙醛經 CGRP 受體與 TRPA1 介導乙醇引發的小鼠異痛，說明乙醇的促偏頭痛作用 |
| [19486361](https://pubmed.ncbi.nlm.nih.gov/19486361/) | 2010 | 基因關聯研究 | Headache | 探討 ADH2 基因型與偏頭痛風險的關聯，屬乙醇代謝研究 |
| [35063053](https://pubmed.ncbi.nlm.nih.gov/35063053/) | 2022 | 世代研究 | Aerosp Med Hum Perform | 軍方飛行員的偏頭痛病史與預後，討論可調整的加重因素 |
| [6352219](https://pubmed.ncbi.nlm.nih.gov/6352219/) | 1983 | 機轉探討 | Drug Alcohol Depend | 前列腺素可能參與酒精不耐與宿醉 |
| [1495822](https://pubmed.ncbi.nlm.nih.gov/1495822/) | 1992 | 評論 | Pathol Biol | 質疑偏頭痛誘因（如飲食）的立論基礎 |

檢索結果中另有數篇 palmitoylethanolamide（PEA）的研究。PEA 與乙醇是不同化合物，只是因名稱字串相符而被檢索到，已排除。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|-------|
| HK-66686 | CHLORHEXIDINE SOLUTION 2% W/V IN ALCOHOL 70% V/V | MARCHING PHARMACEUTICAL LIMITED |
| HK-68185 | CARMUSTINE WAYMADE POWDER AND SOLVENT FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-68201 | MARSEPT CUTANEOUS SOLUTION 2% W/V + 70% V/V | MARCHING PHARMACEUTICAL LIMITED |

上述許可證資料未提供劑型與核准適應症文字。

## 安全性考量

安全性資訊請參考原廠仿單。（藥物交互作用查詢無結果。）

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高（99.29%），但沒有任何臨床試驗或文獻支持乙醇可治療偏頭痛，證據等級僅 L5。
- 現有證據反而顯示乙醇是偏頭痛誘發因子，且已有前臨床機轉（乙醛經 CGRP/TRPA1）指向相反方向，因此不建議推進。

**若要重新評估需要：**
- 出現以乙醇（非異丙醇、非 PEA）治療偏頭痛的臨床或前臨床證據。
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 補充 DrugBank 的作用機轉資料，確認是否存在任何合理的治療性機轉。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

