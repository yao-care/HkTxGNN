---
layout: default
title: Phenytoin
parent: 僅模型預測 (L5)
nav_order: 695
evidence_level: L5
indication_count: 3
monitor_inn: "PHENYTOIN"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
last_modified_at: 2026-10-28
description: "Phenytoin：預測新適應症為三叉神經腫瘤 (Trigeminal Nerve Neoplasm)（證據等級 L5）。原適應症：知識圖譜記錄為癲癇等"
---

# Phenytoin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Phenytoin：從癲癇到三叉神經腫瘤
{: .text-alpha }

## 一句話總結

Phenytoin（苯妥英）是一種抗癲癇藥物，知識圖譜中記錄的使用方向包括癲癇、全身性強直陣攣發作、癲癇重積狀態等。
TxGNN 模型預測分數最高的是**三叉神經腫瘤 (trigeminal nerve neoplasm)**，但證據不支持；真正有文獻支持的方向是排名第二的**三叉神經痛 (trigeminal neuralgia)**，目前有 **0 個臨床試驗**和 **19 篇文獻**（以綜述、指引與回溯性研究為主）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄為癲癇等（香港許可證未提供核准適應症文字） |
| 預測新適應症 | 三叉神經痛 (Trigeminal Neuralgia)（排名第 2，為證據最完整的預測；排名第 1 為三叉神經腫瘤） |
| TxGNN 預測分數 | 三叉神經痛 0.9997（三叉神經腫瘤 0.9999） |
| 證據等級 | 三叉神經痛：L5（見下方說明）；三叉神經腫瘤：L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold（三叉神經腫瘤）；三叉神經痛為 Proceed with Guardrails 的研究性候選 |

**關於證據等級的說明：** 三叉神經痛雖有直接研究該疾病的文獻（含 IV phenytoin 的回溯性研究），但無臨床試驗登記，也未確認有已完成的 RCT。資料編譯時給予 L3（觀察性研究／系統性回顧）。這些文獻直接探討此疾病，因此 L3 成立；但需注意證據多為小型觀察性研究。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。依一般藥理知識，Phenytoin 為電壓門控鈉通道阻斷劑，以使用依賴性方式降低神經元的高頻異常放電。

三叉神經痛被認為與三叉神經根的血管壓迫、局部脫髓鞘及異常神經放電有關。這種機轉與癲癇的神經過度興奮相似，也與一線藥物 carbamazepine 的作用方式相同，因此 Phenytoin 在機轉上適用於此疾病。文獻中，Phenytoin 常被列為二線藥物或急性發作的急救選項。

至於排名第 1 的**三叉神經腫瘤**（TxGNN 模型 (深度學習) 分數 0.9999），高分來自 TxGNN 模型 (深度學習)，可能只是反映模型學到的相關疾病（如三叉神經痛）之間的相似性，並非生物學證據，也不代表抗腫瘤作用。目前沒有任何資料支持 Phenytoin 能治療腫瘤本身；檢索到的兩篇文獻談的是三叉神經痛與 Sturge-Weber 症候群，而非腫瘤。排名第 3 的**β-酮硫解酶缺乏症**（分數 0.9995）沒有任何臨床試驗或文獻，機轉上也無關聯，其分數可能只反映模型學到的疾病間相似性，並非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為三叉神經痛相關的主要文獻（優先列出指引、回溯性研究與直接探討 Phenytoin 者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | 指引 | European Journal of Neurology | 歐洲神經學會的三叉神經痛處置建議 |
| [35469475](https://pubmed.ncbi.nlm.nih.gov/35469475/) | 2022 | 回溯性世代 | Cephalalgia | 144 例，評估靜脈 lacosamide 與 phenytoin 用於三叉神經痛急性發作的效果與安全性 |
| [32981076](https://pubmed.ncbi.nlm.nih.gov/32981076/) | 2020 | 回溯性世代 | Headache | 分析靜脈 phenytoin 作為三叉神經痛危象急救治療的反應 |
| [28761370](https://pubmed.ncbi.nlm.nih.gov/28761370/) | 2017 | 綜述 | Journal of Pain Research | 比較 phenytoin 與 carbamazepine 的行銷導向與實證導向治療 |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | 綜述 | Molecular Pain | 三叉神經痛從病理生理到藥物治療的概述 |
| [29114270](https://pubmed.ncbi.nlm.nih.gov/29114270/) | 2017 | 綜述 | Asian Journal of Neurosurgery | 三叉神經痛的機轉與分型，神經血管衝突為最被接受的成因 |
| [19445753](https://pubmed.ncbi.nlm.nih.gov/19445753/) | 2009 | 綜述 | BMJ Clinical Evidence | 三叉神經痛的臨床特徵與治療證據 |
| [35695796](https://pubmed.ncbi.nlm.nih.gov/35695796/) | 2022 | 綜述 | Expert Opinion on Pharmacotherapy | 三叉神經病變性疼痛的藥物治療更新 |
| [11096730](https://pubmed.ncbi.nlm.nih.gov/11096730/) | 1999 | 綜述 | Current Treatment Options in Neurology | Carbamazepine 為首選；phenytoin 等為二線選項 |
| [628068](https://pubmed.ncbi.nlm.nih.gov/628068/) | 1978 | 文章 | JAMA | 多數病人可用 phenytoin 或 carbamazepine 成功控制疼痛 |

三叉神經腫瘤方面，僅有兩篇間接文獻（[17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) 為三叉神經痛綜述；[9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) 為 Sturge-Weber 症候群病例系列），均未直接研究該腫瘤。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-47301 | PHENYTOIN INJ 250MG/5ML | 注射劑（依品名） | 資料未提供 |
| HK-65291 | DILANTIN EXTENDED CAPSULES 30MG | 膠囊（依品名） | 資料未提供 |
| HK-07909 | DILANTIN CAP 100MG | 膠囊（依品名） | 資料未提供 |
| HK-19932 | DILANTIN INJ 250MG/5ML | 注射劑（依品名） | 資料未提供 |
| HK-07913 | DILANTIN SUSP 125MG/5ML | 懸液劑（依品名） | 資料未提供 |

5 張許可證均為單一成分、有效狀態。許可證資料中沒有核准適應症文字，因此癲癇等適應症僅為知識圖譜中記錄的關係，不能視為香港核准適應症。

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單內容）：長 QT 症候群、尖端扭轉型心室頻脈、肝衰竭、肝病、腎臟病、紫質症、血小板減少、嗜中性白血球減少、顆粒性白血球缺乏症、全身性紅斑狼瘡、糖尿病與酮酸中毒、高血糖、低血壓、肝性腦病變、阻塞性睡眠呼吸中止症等。
- **藥物交互作用**：共查得 100 筆。中度者如 acarbose、famotidine、ranitidine、doxycycline、hydrocortisone、dexamethasone、metformin、pioglitazone、bupropion、aprepitant、morphine、omeprazole、metronidazole 等；acetylsalicylic acid 為輕度。
- **其他考量**：Phenytoin 治療指數窄，靜脈負荷劑量有心臟風險，需監測血中濃度（低白蛋白血症時總濃度可能低估毒性）。

正式的警語與禁忌請參考原廠仿單（本次未取得香港仿單資料）。

## 結論與下一步

**決策：**
- 三叉神經腫瘤：**Hold**
- 三叉神經痛：**Proceed with Guardrails**（作為研究性方向）

**理由：**
- 三叉神經腫瘤缺乏任何直接證據與合理機轉，其高分（0.9999）來自 TxGNN 模型 (深度學習)，可能只反映模型學到的相關疾病間相似性，並非生物學證據；β-酮硫解酶缺乏症（0.9995）同樣無證據。
- 三叉神經痛有指引、回溯性研究與綜述支持 Phenytoin 為二線或急性急救選項，且香港已有口服與注射劑型上市；但缺乏臨床試驗與 RCT，證據仍偏弱。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症資料
- 補充 DrugBank 的作用機轉資料
- 設計或查找三叉神經痛的前瞻性對照研究（尤其是與 carbamazepine 的比較）
- 制訂 IV 使用的心臟監測與血中濃度監測計畫，並審視高風險族群與 DDI
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

