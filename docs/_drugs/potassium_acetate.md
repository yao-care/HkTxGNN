---
layout: default
title: Potassium Acetate
parent: 中證據等級 (L3-L4)
nav_order: 602
evidence_level: L4
indication_count: 1
---

# Potassium Acetate
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

# Potassium Acetate（醋酸鉀）：原適應症資料缺如 → 預測用於腎小管酸中毒（Renal Tubular Acidosis）

## 一句話總結

Potassium Acetate（DrugBank DB14498）目前於香港未上市，原始核准適應症與作用機轉資料皆缺如。TxGNN 模型預測其可能對**腎小管酸中毒 (Renal Tubular Acidosis)** 有效，目前僅有 **9 篇文獻**支持（多為個案報告），無任何臨床試驗或 ICTRP 登記。文獻本身也點出此預測存在機轉矛盾疑慮，建議暫緩推進。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開資料（原始核准適應症未載明） |
| 預測新適應症 | 腎小管酸中毒 (Renal Tubular Acidosis) |
| TxGNN 預測分數 | 99.90%（排名第 2,720） |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Potassium Acetate 詳細的作用機轉（MOA）資料，此為 High 等級的 Data Gap。根據可查文獻的推論：醋酸鉀的乙酸根可經代謝轉為碳酸氫根，理論上具鹼化血液的作用，這符合腎小管酸中毒（RTA）患者需要鹼補充治療的病理生理邏輯，是 TxGNN 給出高分（0.999）的可能理由。

但這個推論有明顯的矛盾之處：檢附的 9 篇文獻中，絕大多數描述的其實是「高血鉀型」RTA（type 4 / hyporeninemic hypoaldosteronism / Gordon syndrome），這類病人補鉀屬於相對禁忌，方向上與給予鉀鹽治療直接衝突。換句話說，TxGNN 的高分較可能反映「hyperkalemia／RTA／potassium」在文獻中的詞彙共現，而非真實的治療關聯。由於 MOA 欄位本身也是 Data Gap，目前無法排除機轉誤配的可能性，需要人工複核以區分不同 RTA 亞型（如低血鉀型的近端 type 2、遠端 type 1，才是理論上適合補鉀治療的族群）。

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 與 ICTRP 皆為 0 筆）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6758113](https://pubmed.ncbi.nlm.nih.gov/6758113/) | 1982 | Review | Schweizerische medizinische Wochenschrift | 選擇性低醛固酮症之機轉回顧，探討高血鉀型酸中毒鑑別診斷 |
| [3398981](https://pubmed.ncbi.nlm.nih.gov/3398981/) | 1988 | Review | Nephron | 個案顯示高血鉀在 hyporeninemic hypoaldosteronism 酸中毒中扮演主要角色 |
| [33771116](https://pubmed.ncbi.nlm.nih.gov/33771116/) | 2021 | Cohort | BMC Nephrology | 隨機試驗比較生理食鹽水與 Plasma-Lyte 對腎損傷標記與鈉排除的影響 |
| [239022](https://pubmed.ncbi.nlm.nih.gov/239022/) | 1975 | Animal Study | The Journal of Clinical Investigation | 大鼠實驗：容積擴張對腎臟檸檬酸與氨代謝的影響（KCl 缺乏模型） |
| [37224266](https://pubmed.ncbi.nlm.nih.gov/37224266/) | 2023 | Case Report | Veterinary Medicine and Science | 犬隻全身麻醉後出現暫時性遠端 RTA 合併腎源性尿崩症 |
| [4015282](https://pubmed.ncbi.nlm.nih.gov/4015282/) | 1985 | Case Report | Archives of Internal Medicine | 鉛腎病變合併高血鉀型遠端 RTA 與選擇性醛固酮不足 |
| [2973296](https://pubmed.ncbi.nlm.nih.gov/2973296/) | 1988 | Case Report | Archives des maladies du coeur et des vaisseaux | 高血鉀性高血壓合併腎小管酸中毒：Gordon 症候群個案 |
| [637641](https://pubmed.ncbi.nlm.nih.gov/637641/) | 1978 | Case Report | Archives of Internal Medicine | 家族性高血鉀、高血壓合併低腎素血症，鉀處理缺陷個案 |
| [34442051](https://pubmed.ncbi.nlm.nih.gov/34442051/) | 2021 | Case Report | Journal of Clinical Medicine | Patiromer（鉀交換樹脂）誘發高血鈣之罕見個案，非直接相關 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L4，無任何臨床試驗支持，9 篇文獻幾乎全為個案報告，且多數描述的是與補鉀治療方向相衝突的「高血鉀型」RTA，機轉合理性存疑。
- TFDA/仿單警語與禁忌症資料為 Blocking 等級 Data Gap，目前無法進入 S1 安全性初評；藥物在香港亦尚未上市（0 張許可證）。

**若要推進需要：**
- 補齊 TFDA/原廠仿單完整警語與禁忌症（Blocking gap，優先項）
- 透過 DrugBank API 補齊 MOA 資料，釐清機轉關聯性
- 人工複核文獻，區分低血鉀型（type 1/2，理論上適合補鉀）與高血鉀型（type 4，補鉀為禁忌）RTA 亞型，確認 TxGNN 高分是否為詞彙共現假訊號
- 若鎖定特定亞型後，補強該族群的臨床證據以提升證據等級
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

