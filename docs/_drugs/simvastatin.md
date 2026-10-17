---
layout: default
title: Simvastatin
parent: 高證據等級 (L1-L2)
nav_order: 815
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Simvastatin：預測新適應症為家族性高膽固醇血症 (Familial Hypercholesterolemia)（證據等級 L1）。原適應症：高三酸甘油酯血症、中風相關疾病、腦梗塞、動脈粥狀硬化、高脂蛋白血症、同型合子家族性高膽固醇血症等"
monitor_inn: "SIMVASTATIN"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency"]
---

# Simvastatin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Simvastatin：從高三酸甘油酯血症與動脈粥狀硬化到家族性高膽固醇血症

## 一句話總結

Simvastatin 是一種史他汀類（statin）降血脂藥，原本用於高脂血症、動脈粥狀硬化與腦中風相關疾病的治療。
TxGNN 模型預測它可能對**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 有效，
目前有 **8 個臨床試驗**和 **18 篇文獻**支持這個方向。
需注意，此預測與原適應症（含同型合子家族性高膽固醇血症）高度重疊，較接近同一疾病家族內的延伸，而非真正的跨疾病再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高三酸甘油酯血症、中風相關疾病、腦梗塞、動脈粥狀硬化、高脂蛋白血症、同型合子家族性高膽固醇血症等（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記載，但根據已知藥理，Simvastatin 是 HMG-CoA 還原酶抑制劑，可降低肝臟膽固醇合成，並上調 LDL 受體，加速血中 LDL-C 清除。這個機轉與家族性高膽固醇血症（LDL 受體功能異常導致 LDL-C 升高）直接相關。

原適應症已包含同型合子家族性高膽固醇血症與多種高脂血症，因此新預測的疾病與原適應症屬同一疾病家族。需要留意的是，同型合子患者的 LDL 受體殘餘功能有限，藥物反應會減弱。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 完成 | 720 | ENHANCE 試驗：Ezetimibe 加高劑量 Simvastatin 對比單用 Simvastatin，評估異合子家族性高膽固醇血症頸動脈粥狀硬化進展（Simvastatin 為對照組，關聯性最直接） |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | 完成 | 248 | Ezetimibe 併用 Simvastatin 用於 10–17 歲異合子家族性高膽固醇血症青少年的療效與安全性 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | Ezetimibe 加 Atorvastatin 或 Simvastatin 用於同型合子家族性高膽固醇血症（樣本小） |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | 上述試驗的 24 個月開放標籤延伸，評估長期安全性與耐受性 |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | 完成 | 249 | Alirocumab 用於控制不佳的異合子 FH（Simvastatin 為背景治療） |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | 完成 | 153 | Alirocumab 用於兒童與青少年異合子 FH（Simvastatin 至多為背景治療） |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | 完成 | 442 | Rosuvastatin 與 Simvastatin 對 IIa/IIb 型血脂異常（含異合子 FH）腎臟影響的 6 週比較，關聯性間接 |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | Alirocumab 用於兒童同型合子 FH，小型開放標籤研究，Simvastatin 至多為背景治療 |

此外另有 Phase 2 試驗 [NCT01890967](https://clinicaltrials.gov/study/NCT01890967)（n=527，LY3015014 劑量範圍研究，Simvastatin 證據間接）。以上多數試驗中，Simvastatin 是併用或背景治療，而非受試主角，僅 ENHANCE 與 NCT00129402 與 Simvastatin 直接相關。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | 臨床試驗 | N Engl J Med | ENHANCE 試驗：Simvastatin 加或不加 Ezetimibe 於家族性高膽固醇血症 |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 兒童家族性高膽固醇血症的史他汀治療 |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 同上（2017 版） |
| [25054950](https://pubmed.ncbi.nlm.nih.gov/25054950/) | 2014 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 同上（2014 版） |
| [20614444](https://pubmed.ncbi.nlm.nih.gov/20614444/) | 2010 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 同上（2010 版） |
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | 指引 | J Am Coll Cardiol | 2026 ACC/AHA 血脂異常管理指引，取代 2018 年膽固醇指引 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | 指引 | Endocr Pract | AACE/ACE 血脂異常管理與心血管疾病預防指引 |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | 臨床研究／回顧 | Drug Saf | Simvastatin 用於家族性高膽固醇血症的效益與風險 |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | 回顧 | Expert Opin Drug Saf | Simvastatin 於家族性高膽固醇血症的效益與風險評估 |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | 橫斷面研究 | J Clin Med | 以 10 mg Simvastatin 治療的 FH 兒童（n=26）之細胞免疫參數 |

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一成分製劑。資料中未載明劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34337 | ZOCOR TAB 10MG（原廠，Organon） | 錠劑 | 未載明 |
| HK-51048 | SIMVASTATIN-TEVA TAB 20MG | 錠劑 | 未載明 |
| HK-51793 | APO-SIMVASTATIN TAB 40MG | 錠劑 | 未載明 |
| HK-58993 | SIMPLAQOR TAB 10MG（Sandoz） | 錠劑 | 未載明 |
| HK-60041 | KARDAK 10 TAB 10MG（Aurobindo） | 錠劑 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（非仿單文字）：肝臟疾病、肌病變／橫紋肌溶解症、胰臟炎、膽囊疾病、糖尿病與高血糖、血小板減少症、痛風、急性冠心症、低血壓等。
- **藥物交互作用**：共記錄 100 筆。重大等級包括 Amiodarone、Amlodipine、Fenofibrate；中度包括 Paclitaxel、Nifedipine、Omeprazole 等。使用 CYP3A4 抑制劑時需特別注意肌病變風險。
- 其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項已完成的 Phase 3 試驗涉及 Simvastatin 與家族性高膽固醇血症，其中 ENHANCE 與青少年 Ezetimibe 併用試驗直接相關。
- 但多數試驗中 Simvastatin 屬併用或背景治療，且此適應症與原適應症高度重疊，屬同疾病家族延伸。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 補充 Simvastatin 單藥在異合子與同型合子 FH 的直接證據，並釐清同型合子的反應減弱情形
- 建立肌病變監測與 CYP3A4 交互作用管理計畫
- 制定兒童與青少年族群的劑量與用藥指引

---

### 其他預測適應症簡述

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 體染色體顯性高膽固醇血症 | 99.36% | L1 | Proceed with Guardrails（與家族性高膽固醇血症證據高度重疊） |
| 腦幹梗塞 | 99.41% | L5 | Hold（僅有一篇與 Simvastatin 無關的動物實驗） |
| 膽固醇酯轉移蛋白缺乏症 | 99.39% | L5 | Hold（僅有模型預測，臨床需求不明確） |
| 膽固醇 7α-羥化酶缺乏所致高膽固醇血症 | 99.27% | L5 | Hold（僅有模型預測，且此病對史他汀反應可能較差） |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

