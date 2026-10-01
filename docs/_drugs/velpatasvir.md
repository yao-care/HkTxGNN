---
layout: default
title: Velpatasvir
parent: 僅模型預測 (L5)
nav_order: 914
evidence_level: L5
indication_count: 5
---

# Velpatasvir
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

# Velpatasvir：從 C 型肝炎到 B 型肝炎病毒感染

## 一句話總結

Velpatasvir 是 C 型肝炎病毒 (HCV) NS5A 抑制劑，在香港以 Epclusa、Vosevi 等複方上市。
TxGNN 預測它可能對 **B 型肝炎病毒感染 (Hepatitis B Virus Infection)** 有效。
目前**沒有任何臨床試驗或文獻直接證明對 HBV 有療效**，檢索到的資料幾乎都是 HCV 研究，唯一與 HBV 直接相關的訊號是安全性警示（HBV 再活化）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明核准適應症；從試驗與文獻判斷為慢性 C 型肝炎） |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5（無 HBV 直接研究；Evidence Pack 標為 L4，但未見 HBV 前臨床或機轉研究支持） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Velpatasvir 是 HCV NS5A 抑制劑，常與 sofosbuvir 組成複方使用，其在 HCV 的療效已有多項 Phase 2/3 試驗支持。

但機轉上，**HBV 沒有 NS5A 的同源蛋白，Velpatasvir 對 HBV 沒有明確的直接抗病毒作用**。TxGNN 的高分較可能來自知識圖譜中「病毒性肝炎」節點之間的關聯，而不是真正的藥理依據。

HBV 與 HCV 雖同為肝炎病毒，但屬於不同的病毒科，複製機制也不同。兩者的臨床交集主要在 HBV/HCV 共感染：接受 HCV 直接抗病毒藥物 (DAA) 治療時，HBV 可能再活化。這是需要提防的風險，不是療效證據。

## 臨床試驗證據

以下試驗全部是 HCV 研究，**沒有任何一項以 HBV 療效為主要終點**。其中 NCT04997564 涉及 HCV/HBV 共感染，最接近此預測。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | 中國 HCV/HBV 共感染患者，SOF/VEL 治療 12 週並預防性使用 TAF，觀察 HBV 再活化（尚無結果） |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | 完成 | 102 | SOF/VEL ± ribavirin 用於 HCV 失代償性肝硬化（HCV 研究，非 HBV） |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | 完成 | 268 | SOF/VEL 用於 HCV 合併 Child-Pugh B 級肝硬化（HCV 研究，非 HBV） |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | 完成 | 379 | SOF + VEL 用於未治療過的 HCV 基因型 1–6（HCV 研究，非 HBV） |
| [NCT01826981](https://clinicaltrials.gov/study/NCT01826981) | Phase 2 | 完成 | 359 | 含 sofosbuvir 的方案用於慢性 HCV（HCV 研究，非 HBV） |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV-HCV 共感染且接受鴉片替代療法者，換藥後使用 SOF/VEL（無 HBV 終點） |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | 完成 | 228 | 學名 VEL/SOF 用於 HIV/HCV 共感染（HCV 研究，非 HBV） |
| [NCT03513393](https://clinicaltrials.gov/study/NCT03513393) | Phase 1 | 完成 | 11 | 可樂對 omeprazole 治療者吸收 velpatasvir 的影響（藥物動力學研究） |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | 完成 | 281 | ribavirin 加 SOF/VEL/VOX 用於 HCV 治療失敗者再治療（HCV 研究，非 HBV） |
| [NCT03579576](https://clinicaltrials.gov/study/NCT03579576) | N/A | 完成 | 803 | 緬甸簡化 HCV 檢測與治療模式，整合 HIV 篩檢（HCV 研究，非 HBV） |

## 文獻證據

沒有 RCT。以下依綜述、病例報告、觀察性研究排序，**沒有任何一篇顯示 Velpatasvir 對 HBV 有療效**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | 兒童病毒性肝炎的進展與挑戰；HCV 已有 DAA 可用，HBV 治療仍遠未達到治癒 |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | 慢性 C 型肝炎的診斷與治療簡介（HCV） |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | HCV 抗病毒藥物的藥動學與藥效學整理（HCV） |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | 一名 HBV 核心抗體陽性患者在 SOF/VEL 治療 HCV 期間發生 HBV 再活化，且帶有表面抗原免疫逃逸突變株 |
| [32935438](https://pubmed.ncbi.nlm.nih.gov/32935438/) | 2021 | 觀察性研究 | J Viral Hepat | 緬甸簡化 HCV 治療策略；HBV 共感染者同時使用 tenofovir，主要評估 HCV 治療結果與成本 |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | 真實世界研究 | J Virus Eradication | 中國患者使用 SOF/VEL 為主的 HCV 治療，含 HCV/HBV 共感染族群 |
| [41734217](https://pubmed.ncbi.nlm.nih.gov/41734217/) | 2025 | 回溯性研究 | Klin Mikrobiol Infekc Lek | 捷克 Ostrava 兒童 B 型與 C 型肝炎的抗病毒治療頻率、療效與耐受性 |
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | 單臂試驗 | Lancet Gastroenterol Hepatol | 盧安達 SOF/VEL 治療未治療過的 HCV（HCV 研究） |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | 世代研究 | J Gastroenterol Hepatol | SOF/VEL 在 HCV 基因型 3 的真實世界療效（HCV 研究） |
| [37286314](https://pubmed.ncbi.nlm.nih.gov/37286314/) | 2023 | 回溯性分析 | BMJ Open | 台灣南部監獄 C 型肝炎患者的治療效果與副作用（HCV 研究） |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-65046 | EPCLUSA TABLETS 400MG/100MG | GILEAD SCIENCES HONG KONG LIMITED |
| HK-65775 | VOSEVI TABLETS | GILEAD SCIENCES HONG KONG LIMITED |

兩張許可證都未載明核准適應症與劑型。依試驗資料判斷，Epclusa 為 sofosbuvir/velpatasvir 複方，Vosevi 為 sofosbuvir/velpatasvir/voxilaprevir 複方。

## 安全性考量

- **HBV 再活化風險**：病例報告 (PMID 31542053) 顯示，HBV 核心抗體陽性的患者在 SOF/VEL 治療 HCV 期間可能發生 HBV 再活化。這是對 HBV 感染者使用本藥時最需要注意的風險。NCT04997564 正以預防性 TAF 搭配 SOF/VEL 驗證這個問題。
- **藥物交互作用**：NCT03513393 指出 velpatasvir 的吸收受 pH 影響，質子幫浦抑制劑（如 omeprazole）可使其吸收降低約 26–56%。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻支持 Velpatasvir 對 HBV 有效。HBV 缺乏 NS5A 靶點，TxGNN 99.87% 的分數較可能反映知識圖譜中「病毒性肝炎」的關聯，而非藥理依據。
- 現有的 HBV 相關訊號是安全性警示（再活化），不是療效證據。

**若要推進需要：**
- 取得 Velpatasvir 的作用機轉資料（DrugBank），並評估是否有任何抗 HBV 的體外活性。
- 以 HBV 為終點的體外或前臨床研究，作為最低限度的機轉證據。
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 追蹤 NCT04997564 的結果，了解 HCV/HBV 共感染時 HBV 再活化的風險與預防策略。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

