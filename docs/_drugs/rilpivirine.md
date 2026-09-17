---
layout: default
title: Rilpivirine
parent: 僅模型預測 (L5)
nav_order: 649
evidence_level: L5
indication_count: 5
---

# Rilpivirine
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

# Rilpivirine：從 HIV-1 感染到多項愛滋病相關新適應症

## 一句話總結

Rilpivirine（DB08864）是非核苷反轉錄酶抑制劑（NNRTI），常與 cabotegravir 併用組成長效針劑（CAB+RPV LA），核准用於成人 HIV-1 感染治療（此資訊來自證據包內臨床試驗描述，非官方仿單）。TxGNN 針對此藥產生 **5 項預測適應症**，證據強度差異極大：**AIDS 相關複合症**與**先天性 HIV 感染（孕期母嬰垂直傳染防治）**有直接以 rilpivirine 為受試藥物的人體 Phase 3 試驗支持，證據等級達 L1／L3；另兩項為**貓愛滋病毒（FIV）**與**猿猴免疫缺陷病毒（SIV/SHIV）**動物模式的跨物種推論；最後一項**罕見神經發育疾病**則無任何機轉或證據支持，極可能為模型假陽性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（依臨床試驗描述推知；證據包無正式仿單/許可證資料） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 候選新適應症數 | 5 項 |
| 最佳候選 | AIDS related complex（L1，Proceed with Guardrails） |
| 次佳候選 | 先天性 HIV 感染（L3，Proceed with Guardrails） |
| 建議決策 | 依候選而異（詳見下方各項評估） |

### 預測適應症一覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議決策 |
|---|---|---|---|---|---|
| 5 | AIDS related complex | 99.56% | L1 | S3 | Proceed with Guardrails |
| 4 | 先天性 HIV 感染 (congenital HIV) | 99.56% | L3 | S2 | Proceed with Guardrails |
| 2 | 猿猴免疫缺陷病毒感染 (SIV/SHIV) | 99.97% | L4 | S1 | Research Question |
| 1 | 貓愛滋病症候群 (feline AIDS/FIV) | 99.97% | L4 | S0 | Hold |
| 3 | 罕見神經發育疾病 | 99.97% | L5 | S0 | Hold |

> 註：TxGNN 分數反映知識圖譜嵌入相似度，**不代表臨床證據強度**；分數最高的候選（FIV、SIV）證據等級反而較低。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。但根據證據包內多筆臨床試驗描述可確認：rilpivirine 是**非核苷反轉錄酶抑制劑（NNRTI）**，透過抑制 HIV-1 反轉錄酶阻斷病毒複製，常與整合酶抑制劑 cabotegravir 組成長效肌肉注射雙藥療法（CAB+RPV LA，商品名 Cabenuva），用於病毒學已抑制之成人 HIV-1 感染者。

**人類適應症延伸（AIDS 相關複合症、先天性 HIV）**：這兩項本質上是既有 HIV-1 治療機轉在**不同臨床階段／族群**的延伸應用，而非新標靶假說——「AIDS related complex」是 HIV 感染進展至 AIDS 前症狀期的舊分類術語，「先天性 HIV 感染」防治核心即孕婦母體病毒抑制。兩者都已有以 rilpivirine 為受試藥物的人體試驗直接驗證。

**動物模式延伸（FIV、SIV/SHIV）**：FIV（貓）與 SIV/SHIV（獼猴）是不同屬的慢病毒，與 HIV-1 的反轉錄酶結構有差異。現有文獻僅屬生化交叉抑制比較或標準轉譯前臨床平台試驗，尚未回答「對人類新適應症是否有效」，故機轉關聯性僅供研究方向參考。

**罕見神經發育疾病**：無任何機轉、文獻或試驗支持，抗病毒藥物與此疾病病理生理無已知連結，判斷為模型假陽性。

---

## 候選適應症詳解

### 🥇 AIDS related complex（證據等級 L1，Proceed with Guardrails）

**臨床試驗證據**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01792570](https://clinicaltrials.gov/study/NCT01792570) | Phase 3 | 完成 | 37 | Darunavir/ritonavir + rilpivirine 雙藥療法 vs 三藥療法，病毒學已抑制病人之非劣效性與非 HIV 相關併發症評估（Grade A：直接以 RPV 為受試藥物） |
| [NCT01076179](https://clinicaltrials.gov/study/NCT01076179) | N/A | 完成 | 502 | Kaletra（lopinavir/ritonavir）併用新型 INI/CCR5 拮抗劑/NNRTI 的耐受性研究（Grade C：RPV 非核心介入） |

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37568163](https://pubmed.ncbi.nlm.nih.gov/37568163/) | 2023 | 個案報告 | AIDS Res Ther | HIV 患者心臟移植後 ART 與免疫抑制劑之藥物交互作用管理 |

---

### 🥈 先天性 HIV 感染 / 母嬰垂直傳染防治（證據等級 L3，Proceed with Guardrails）

**臨床試驗證據**（依相關性排序，列出 10 個最相關試驗）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07412977](https://clinicaltrials.gov/study/NCT07412977) | N/A | 尚未招募 | 5160 | VIROPREG：法國前瞻性世代研究，評估孕期病毒感染（含 HIV）與抗病毒治療對母嬰健康之影響 |
| [NCT00855335](https://clinicaltrials.gov/study/NCT00855335) | Phase 3 | 完成 | 77 | HIV-1 孕婦中 darunavir/ritonavir、darunavir/cobicistat、etravirine、rilpivirine 之藥物動力學研究 |
| [NCT00042289](https://clinicaltrials.gov/study/NCT00042289) | N/A | 完成 | 1578 | IMPAACT P1026s：孕期及產後 ARV／抗結核藥物藥物動力學前瞻性研究 |
| [NCT03497676](https://clinicaltrials.gov/study/NCT03497676) | Phase 1/2 | 完成 | 168 | 口服與長效注射 CAB+RPV 於病毒學已抑制之兒童與青少年的安全性、耐受性與 PK |
| [NCT02494986](https://clinicaltrials.gov/study/NCT02494986) | Phase 2 | 進行中未招募 | 48 | RPV 併用背景療法於曾參與 RPV 兒科試驗之患者的續用性研究 |
| [NCT03299049](https://clinicaltrials.gov/study/NCT03299049) | Phase 3 | 進行中未招募 | 1049 | ATLAS-2M：長效 CAB+RPV 每 8 週 vs 每 4 週注射之非劣效性試驗（核心藥效基礎） |
| [NCT02422797](https://clinicaltrials.gov/study/NCT02422797) | Phase 3 | 完成 | 518 | 由現行 ART 轉換為 DTG+RPV 雙藥療法之非劣效性試驗 |
| [NCT02951052](https://clinicaltrials.gov/study/NCT02951052) | Phase 3 | 進行中未招募 | 618 | ATLAS：由現行 ART 轉換為長效肌肉注射 CAB+RPV 之維持抑制試驗 |
| [NCT03984838](https://clinicaltrials.gov/study/NCT03984838) | Phase 1 | 完成 | 16 | DTG+RPV（JULUCA）複方錠於日裔健康受試者之 PK、安全性研究 |
| [NCT01641809](https://clinicaltrials.gov/study/NCT01641809) | Phase 2 | 完成 | 244 | 口服 GSK1265744（cabotegravir）+RPV 誘導後維持病毒學抑制之劑量範圍研究 |

**文獻證據**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41225339](https://pubmed.ncbi.nlm.nih.gov/41225339/) | 2025 | 系統性回顧/統合分析 | BMC Infect Dis | Cabotegravir 在孕期使用之安全性系統性回顧 |
| [41268510](https://pubmed.ncbi.nlm.nih.gov/41268510/) | 2025 | 個案報告+文獻回顧 | Case Rep Infect Dis | CAB/RPV 貫穿整個孕期用於 HIV 抗病毒治療之個案 |
| [36411596](https://pubmed.ncbi.nlm.nih.gov/36411596/) | 2023 | 世代研究（PK/預後） | HIV Medicine | 臨床試驗中暴露於長效 CAB+RPV 之孕婦妊娠結果與藥物動力學 |
| [38864586](https://pubmed.ncbi.nlm.nih.gov/38864586/) | 2024 | 世代研究 | AIDS (London) | 美國世代中懷孕初期暴露新型 ARV 與先天性異常之關聯 |
| [38703388](https://pubmed.ncbi.nlm.nih.gov/38703388/) | 2024 | 個案報告 | Clin Infect Dis | 長效注射 CAB/RPV 於一名 HIV 孕婦：RPV 濃度較非孕婦低 70-75%，建議此療法可能不適用於孕婦 |

> ⚠️ 需注意：唯一直接個案報告（PMID 38703388）指出孕期 RPV 血中濃度顯著降低，暗示長效注射劑型可能**不適合**孕期使用，此為推進此適應症前必須釐清的安全性疑慮。

---

### 猿猴免疫缺陷病毒感染 SIV/SHIV（證據等級 L4，Research Question）

無臨床試驗登記，僅有動物模式文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41370971](https://pubmed.ncbi.nlm.nih.gov/41370971/) | 2026 | 動物模式（PEP） | EBioMedicine | 長效 CAB+RPV 單次注射於獼猴暴露後預防（PEP）之前臨床評估 |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | 動物模式（療效/緩解） | Nature Communications | 早期治療起始 + 長效抗病毒藥物於 SHIV 感染獼猴之病毒緩解 |
| [26438501](https://pubmed.ncbi.nlm.nih.gov/26438501/) | 2015 | 動物模式（抗藥性） | Antimicrob Agents Chemother | 長效 RPV 於含 HIV-1 RT 之 SIV 感染獼猴中抗藥性變異株發生率低 |
| [29746267](https://pubmed.ncbi.nlm.nih.gov/29746267/) | 2018 | 綜述 | Curr Opin HIV AIDS | Cabotegravir 於 ART 及 PrEP 之潛力綜述 |

此為獼猴動物疾病模型，非人類適應症，無對應人體臨床試驗登錄。

---

### 貓愛滋病症候群 FIV（證據等級 L4，Hold）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | 生化/結構（體外） | J Vet Sci | Nevirapine、efavirenz、rilpivirine 對貓與人類免疫缺陷病毒之生化結構比較 |

僅生化/結構層級跨物種交叉抑制比較，非治療效力證據，屬純獸醫學探索性研究。

---

### 罕見神經發育疾病（證據等級 L5，Hold）

目前無相關臨床試驗登記；目前無相關文獻。純為知識圖譜嵌入相似度預測，無機轉關聯，判斷為假陽性。

---

## 香港上市資訊

Rilpivirine（DB08864）**目前未在香港上市**，無任何許可證登記（`total_licenses = 0`）。此為推進任何新適應症前必須解決的基礎缺口。

---

## 安全性考量

安全性資訊請參考原廠仿單。證據包標記 **TFDA/仿單警語與禁忌為 Blocking 等級資料缺口**，尚未取得，目前無法完成安全性初評（S1 階段）。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限「AIDS related complex」與「先天性 HIV 感染」兩項候選；其餘三項維持 Hold / Research Question）

**理由：**
- AIDS related complex 有直接以 rilpivirine 為受試藥物的 Phase 3 試驗（NCT01792570），證據等級達 L1。
- 先天性 HIV/垂直傳染防治有多筆孕期 PK 世代研究與系統性回顧支持機轉延伸的合理性（L3），但唯一個案報告顯示長效注射劑型於孕期血中濃度顯著降低，需先釐清安全性疑慮。
- FIV、SIV/SHIV 屬動物模式，機轉推論尚未轉譯至人類新適應症，維持 Research Question / Hold。
- 神經發育疾病候選無任何支持證據，建議直接排除。

**若要推進需要：**
- 取得 rilpivirine 完整 TFDA/原廠仿單警語與禁忌（DG001，Blocking，阻擋 S1 安全性初評）
- 補充作用機轉（MOA）正式資料（DG002）
- 針對孕期適應症，需進一步 PK 研究釐清長效注射劑型於孕期的暴露量是否足夠（回應 PMID 38703388 之疑慮）
- 若考慮在香港申請上市，需先啟動許可證申請流程（現況為 0 張許可證、未上市）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

