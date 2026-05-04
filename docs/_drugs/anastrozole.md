---
layout: default
title: Anastrozole
parent: 高證據等級 (L1-L2)
nav_order: 53
evidence_level: L1
indication_count: 10
---

# Anastrozole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Anastrozole：從芳香酶抑制到女性乳腺癌

## 一句話總結

Anastrozole 是第三代非固醇類芳香酶抑制劑，透過強效抑制 CYP19A1 酶，將停經後女性的循環雌二醇水平壓低逾 85%，切斷雌激素受體陽性（ER+）乳癌細胞的增殖驅動訊號。
TxGNN 模型以極高分數預測它對**女性乳腺癌 (Female Breast Carcinoma)** 有效，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未登記（國際廣泛核准用於 ER+ 停經後乳癌輔助治療及化學預防） |
| 預測新適應症 | 女性乳腺癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Anastrozole 透過選擇性抑制芳香酶（CYP19A1），阻斷末梢組織（脂肪、肌肉、肝臟）中雄激素轉化為雌激素的最後一步。停經後女性幾乎全部的循環雌激素來自此酶，因此 Anastrozole 能將血漿雌二醇壓低超過 85%，遠優於 Tamoxifen 的部分阻斷機轉。ER+ 乳癌細胞依賴雌激素驅動 ERα 訊號、細胞週期蛋白 D1 表達及增殖，切斷此通路可有效抑制腫瘤生長並降低復發風險。

里程碑式的 ATAC 試驗（9,366 名停經後患者，中位追蹤 68 個月）確立 Anastrozole 輔助治療顯著優於 Tamoxifen（HR 0.87，無病存活），奠定其為 ER+ 停經後乳癌輔助治療的國際標準。IBIS-II 試驗則進一步擴展至化學預防層面，10 年隨訪數據顯示即使停藥後保護效益仍持續，支持其在高風險族群的預防性應用。

此 TxGNN 預測屬「模型正確識別已知適應症」的案例：Anastrozole 已獲美國 FDA、EMA 及多個主要藥政機構核准用於女性乳腺癌，但目前在香港並無登記許可證。本報告的核心價值在於評估引進香港市場的可行性，而非開拓全新適應症。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00849030](https://clinicaltrials.gov/study/NCT00849030) | Phase 3 | 完成 | 9,358 | ATAC 試驗：比較 Arimidex 單藥、Nolvadex 單藥及兩者聯合作為停經後乳癌輔助治療，確立 Anastrozole 優先地位 |
| [NCT00066573](https://clinicaltrials.gov/study/NCT00066573) | Phase 3 | 完成 | 7,576 | MA.27 試驗：Exemestane vs Anastrozole 輔助治療 ER+ 停經後乳癌頭對頭比較，評估化療後復發預防 |
| [NCT00248170](https://clinicaltrials.gov/study/NCT00248170) | Phase 3 | 完成 | 4,172 | Letrozole vs Anastrozole 輔助治療 HR+、淋巴結陽性停經後乳癌，5 年隨訪評估生存及復發 |
| [NCT00072462](https://clinicaltrials.gov/study/NCT00072462) | Phase 3 | 完成 | 2,980 | IBIS-II DCIS：Anastrozole vs Tamoxifen 用於停經後 ER+ 乳管原位癌術後預防局部及對側乳癌復發 |
| [NCT00556374](https://clinicaltrials.gov/study/NCT00556374) | Phase 3 | 完成 | 3,420 | 評估 Denosumab 在接受 NSAI（含 Anastrozole）治療的非轉移性乳癌患者中預防首次臨床骨折的療效 |
| [NCT00301457](https://clinicaltrials.gov/study/NCT00301457) | Phase 3 | 完成 | 1,914 | Tamoxifen 2-3 年序貫後，比較 Anastrozole 3 年 vs 6 年輔助療程對 HR+ 停經後乳癌無病存活的影響 |
| [NCT00143390](https://clinicaltrials.gov/study/NCT00143390) | Phase 3 | 完成 | 298 | Exemestane vs Anastrozole 初始荷爾蒙治療停經後晚期/復發乳癌非劣性比較，評估腫瘤進展時間 |
| [NCT01626222](https://clinicaltrials.gov/study/NCT01626222) | Phase 3 | 完成 | 301 | 4EVER 試驗：Everolimus 聯合 Exemestane 治療接受 NSAI（含 Anastrozole）後進展的 ER+/HER2- 停經後晚期乳癌 |
| [NCT06311383](https://clinicaltrials.gov/study/NCT06311383) | N/A（觀察性） | 完成 | 2,610 | 德國真實世界觀察研究：評估 Ribociclib + AI/Fulvestrant 等一線方案在 HR+/HER2- 晚期乳癌的實務有效性與生活品質 |
| [NCT01151215](https://clinicaltrials.gov/study/NCT01151215) | Phase 2 | 終止 | 482 | MINT 試驗：AZD8931 聯合 Anastrozole vs Anastrozole 單藥治療 HR+、內分泌治療初治局部晚期或轉移性乳癌 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15639680](https://pubmed.ncbi.nlm.nih.gov/15639680/) | 2005 | Phase 3 RCT（里程碑） | Lancet | ATAC 試驗 5 年輔助治療結果：Anastrozole 顯著優於 Tamoxifen 延長無病存活（HR 0.87），確立 ER+ 停經後乳癌輔助治療新標準 |
| [31839281](https://pubmed.ncbi.nlm.nih.gov/31839281/) | 2020 | Phase 3 RCT（化學預防） | Lancet | IBIS-II 長期隨訪：Anastrozole 較安慰劑顯著降低高風險停經後女性乳癌發生率，停藥後保護效益持續，支持化學預防應用 |
| [26686313](https://pubmed.ncbi.nlm.nih.gov/26686313/) | 2016 | RCT | Lancet | IBIS-II DCIS：Anastrozole 在停經後 ER+ DCIS 患者中優於 Tamoxifen，降低局部及對側乳癌復發風險 |
| [28415634](https://pubmed.ncbi.nlm.nih.gov/28415634/) | 2017 | Meta-analysis | Oncotarget | 系統性回顧及統合分析多個 RCT：Anastrozole 在無病存活、遠端復發等指標優於 Tamoxifen，安全性特徵可控 |
| [20923259](https://pubmed.ncbi.nlm.nih.gov/20923259/) | 2010 | Drug Monograph | Expert Opin Drug Safety | 全面回顧 Anastrozole 在 ER+ 乳癌輔助治療的療效與安全性，多項 RCT 一致顯示其優於 Tamoxifen |
| [28614542](https://pubmed.ncbi.nlm.nih.gov/28614542/) | 2017 | Literature Review | Rev Assoc Med Bras | 系統性回顧 Anastrozole 在乳癌化學預防與治療的藥理、藥動學特性及臨床應用 |
| [14687437](https://pubmed.ncbi.nlm.nih.gov/14687437/) | 2003 | Review | Curr Med Res Opin | 概述 Anastrozole 臨床試驗歷程，包括較 Megestrol Acetate 二線治療及較 Tamoxifen 一線治療的優勢 |
| [16034487](https://pubmed.ncbi.nlm.nih.gov/16034487/) | 2005 | Drug Profile | Drugs of Today | 回顧 Anastrozole 作用機轉及主要臨床試驗，確認為 ER+ 乳癌輔助治療中唯一在當時獲完整核准的 AI |
| [16761927](https://pubmed.ncbi.nlm.nih.gov/16761927/) | 2006 | Review | Expert Rev Anticancer Ther | ATAC 試驗深入分析：Anastrozole 展現顯著療效及耐受性優勢，骨骼事件為主要需監測副作用 |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Comparative Review | Expert Opin Pharmacother | 比較 Anastrozole、Letrozole、Exemestane 三種第三代 AI 在早期乳癌的療效、安全性及藥理差異 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶內分泌治療（非固醇類芳香酶抑制劑），非傳統細胞毒性化療藥 |
| 骨髓抑制風險 | 低（非直接細胞毒性機轉，不抑制骨髓造血） |
| 致吐性分級 | 低 |
| 監測項目 | 骨密度（DEXA，建議每 1-2 年監測）、肝功能、血脂、關節症狀 |
| 處置防護 | 一般口服藥物處置規範，無需細胞毒性藥物特殊防護措施 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Anastrozole 擁有包括 ATAC、IBIS-II 等多個大型 Phase 3 RCT 的 L1 等級強力證據，已是全球 ER+ 停經後乳癌輔助治療及化學預防的國際標準方案之一；TxGNN 的高分預測（全疾病庫 Rank 6,566，99.68% 信心分數）與現有生物學機轉完全吻合，屬「模型正確識別已知適應症」的高可信案例。香港目前缺乏登記許可，是引進的主要障礙而非療效或安全性疑慮。

**若要推進需要：**
- 向香港衛生署藥物辦公室提交藥物登記申請，引用 EMA／FDA 已核准的完整仿單資料
- 補充 TFDA 仿單警語、禁忌症及藥物交互作用（DDI）詳細資訊，填補現有資料缺口
- 確認香港本地 ER+ 停經後乳癌治療指引及用藥標準，評估與現行化療方案的整合路徑
- 建立骨密度（BMD）監測計畫及關節肌肉症狀管理的臨床路徑（已知長期使用副作用）
- 評估是否需申請優先審查資格，加速市場引進時程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

