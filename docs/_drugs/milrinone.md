---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 588
evidence_level: L5
indication_count: 9
monitor_inn: "MILRINONE"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
last_modified_at: 2026-10-23
description: "Milrinone：預測新適應症為脫髮 (Alopecia)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
---

# Milrinone
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

## Milrinone：從心臟衰竭相關用途到脫髮（預測新適應症）
{: .text-alpha }

> 註：香港許可證資料中未載明核准適應症文字，因此原適應症無法由許可證確認。

## 一句話總結

Milrinone 是一種 PDE3 抑制劑（強心舒血管藥），以注射劑型在香港上市。
TxGNN 模型預測分數最高的新適應症是**脫髮 (Alopecia)**，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測（證據等級 L5）。
在後段預測中，**急性肺心病 (Acute Pulmonary Heart Disease)** 有 1 個臨床試驗和多篇文獻，是證據較完整的方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字 |
| 預測新適應症 | 脫髮 (Alopecia) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Milrinone 是 PDE3 抑制劑，會提高細胞內 cAMP，產生強心與血管擴張作用。

就脫髮而言，只能推測 cAMP 訊號或毛囊血流可能有關，但沒有任何臨床或文獻資料支持。Milrinone 需靜脈給藥，且有心律不整與低血壓風險，不適合用於非危及生命的疾病。這個高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

同一份預測清單中，排名前 4 的都是毛髮相關疾病（脫髮、頭皮單純性毛髮稀少症、先天性毛髮稀少伴粟丘疹、瀰漫性圓禿），全都沒有臨床試驗或文獻。

## 臨床試驗證據

針對脫髮：目前無相關臨床試驗登記。

作為參考，證據最多的預測方向是急性肺心病，其試驗如下（並非直接研究脫髮）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03207165](https://clinicaltrials.gov/study/NCT03207165) | Phase 4 | 完成 | 192 | 比較 Milrinone 與 Dobutamine 用於心臟加護病房重症患者；族群異質，非專指急性肺心病 |

## 文獻證據

針對脫髮：目前無相關文獻。

以下為急性肺心病方向的部分代表文獻（並非直接研究脫髮）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20056439](https://pubmed.ncbi.nlm.nih.gov/20056439/) | 2010 | RCT | J Cardiothorac Vasc Anesth | 比較吸入型硝化甘油與吸入型 Milrinone 對先天性心臟病合併肺動脈高壓兒童的血流動力學影響 |
| [8797620](https://pubmed.ncbi.nlm.nih.gov/8797620/) | 1996 | 雙盲多中心研究 | Crit Care Med | 靜脈 Milrinone 用於日本急性心衰竭患者的血流動力學反應 |
| [8903534](https://pubmed.ncbi.nlm.nih.gov/8903534/) | 1996 | 隨機開放試驗 | Clin Cardiol | 急性心肌梗塞後心衰竭，比較 Milrinone 與 Dobutamine |
| [34218906](https://pubmed.ncbi.nlm.nih.gov/34218906/) | 2021 | 世代研究／病例系列 | Br J Anaesth | 吸入型 Milrinone 改善重症 COVID-19 插管患者的氧合 |
| [8659556](https://pubmed.ncbi.nlm.nih.gov/8659556/) | 1996 | Review | Am J Med Sci | Milrinone 的基礎與臨床藥理及急慢性處置 |
| [28793822](https://pubmed.ncbi.nlm.nih.gov/28793822/) | 2017 | 前臨床 | J Cardiovasc Pharmacol Ther | 慢性實驗性肺高壓中三種強心舒血管藥的劑量反應比較 |

另有頭痛相關方向（僅限可逆性腦血管收縮症候群 RCVS 的病例報告，如 PMID 18647181、34784343），並不等同於一般頭痛或偏頭痛。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67864 | MILRICOR SOLUTION FOR INJECTION/INFUSION 10MG/10ML | 未載明 | 未載明 |
| HK-68587 | MILRINONE LACTATE INJECTION USP 10MG/10ML | 未載明 | 未載明 |
| HK-36347 | PRIMACOR INJ 1MG/ML | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中記錄的禁忌關係**（非仿單內容）：腎臟疾病、低血壓、心肌梗塞、冠狀動脈血栓、猝死性心跳停止、心臟傳導疾病、肺動脈瓣狹窄、肥厚型心肌病變、血紅素病變、輸尿管積膿等。
- **藥物交互作用**（中度）：Amifostine、Diatrizoate、Anagrelide、Ozanimod、Procarbazine。
- **藥理靶點**：PDE2A、PDE3A、PDE3B、PDE5A。
- 文獻提示 Milrinone 輸注期間有發生心室性心律不整的報告（PMID 3953354）。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 脫髮預測僅來自模型，沒有任何臨床試驗或文獻直接研究，屬 L5。
- Milrinone 為需監測的靜脈藥物，有低血壓與心律不整風險，與非致命性毛髮疾病的風險效益不相稱。

**若要推進需要：**
- 毛囊或 cAMP 路徑相關的機轉與前臨床研究
- 評估局部（外用）給藥的可行性，因目前香港許可證皆為注射劑
- 取得香港仿單的警語與禁忌資料，以及完整的作用機轉資料
- 若考慮其他方向，急性肺心病（Milrinone 在急性心衰竭與休克中已有使用基礎）可優先評估，但需有血流動力學監測、低血壓與心律不整防範、腎功能劑量調整，並審慎考量吸入給藥途徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

