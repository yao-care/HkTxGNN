---
layout: default
title: Alirocumab
parent: 高證據等級 (L1-L2)
nav_order: 33
evidence_level: L2
indication_count: 10
---

# Alirocumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Alirocumab：從高膽固醇血症到膽固醇代謝相關障礙

## 一句話總結

Alirocumab（品牌名：Praluent）是全球核准的 PCSK9 抑制劑單株抗體，原用於家族性高膽固醇血症及動脈粥狀硬化性心血管疾病患者的 LDL-C 降低治療，目前在香港尚未取得上市許可。
TxGNN 模型共預測 10 個潛在新適應症，其中以 **膽固醇代謝障礙 (Cholesterol Catabolic Process Disease)**（Rank 5）最具臨床意義，
目前有 **1 個已完成的 Phase 3 臨床試驗**（同類效應）及 **19 篇文獻**（含多篇 2024–2025 年更新）支持此方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 家族性高膽固醇血症（HeFH/HoFH）、動脈粥狀硬化性心血管疾病（ASCVD）降脂治療（全球核准，香港未上市） |
| 預測新適應症（最佳證據） | 膽固醇代謝障礙 (Cholesterol Catabolic Process Disease) |
| TxGNN 預測分數 | 99.36%（Rank 5） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## TxGNN 預測摘要（全部 10 個適應症）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 1 | X 染色體連鎖魚鱗癬（無類固醇硫酸酶缺乏） | 99.43% | L5 | Hold |
| 2 | 其他維生素與輔因子代謝/運輸障礙 | 99.41% | L5 | Hold |
| 3 | 黃色瘤病 (Xanthomatosis) | 99.37% | L4 | Research Question |
| 4 | 46,XY 性別發育異常（DHT 旁路生合成缺陷） | 99.37% | L5 | Hold |
| **5** | **膽固醇代謝障礙 (Cholesterol Catabolic Process Disease)** | **99.36%** | **L2** | **Proceed with Guardrails** |
| 6 | 46,XY 性別發育異常（膽固醇合成缺陷） | 99.35% | L5 | Hold |
| 7 | 斑點橫紋肌發育不良 | 99.30% | L5 | Hold |
| 8 | 中性脂質儲積症 | 99.29% | L5 | Hold |
| 9 | 3-羥基醯基輔酶 A 去氫酶缺乏症 | 99.29% | L5 | Hold |
| 10 | 痙攣性截癱-視神經萎縮-神經病變症候群 | 99.26% | L5 | Hold |

> **說明**：Rank 1–2、4、6–10 缺乏與 PCSK9/LDL 軸的機轉關聯或生物合理性，建議暫緩（Hold）。Rank 3（黃色瘤病）具間接文獻支持，建議列為研究問題（Research Question）。本報告聚焦最具臨床意義的 Rank 5 預測。

---

## 為什麼這個預測合理？

Alirocumab 是一種全人源單株抗體，透過結合並中和循環中游離的 PCSK9（前蛋白轉化酶枯草溶菌素/kexin 9 型）發揮作用。PCSK9 在生理狀態下會引導肝細胞表面的 LDL 受體進行溶酶體降解；阻斷 PCSK9 後，LDL 受體得以循環再利用並持續錨定於肝細胞膜，從而大幅提升 LDL-C 的清除效率，降低血漿 LDL-C 濃度達 40–65%。

膽固醇代謝障礙（cholesterol catabolic process disease）涵蓋家族性高膽固醇血症（FH）、高脂蛋白血症、動脈粥狀硬化等以 LDL-C 代謝失調為共同核心病理的疾病群。Alirocumab 本身即以降低 LDL-C 為主要治療機轉，因此此 TxGNN 預測屬「機轉驗證性預測」——藥物機轉與疾病病理高度吻合，而非意外的跨領域發現。在香港尚未上市的監管背景下，此預測具有重要的市場準入參考價值。

大型 ODYSSEY OUTCOMES 試驗涵蓋逾 47,000 患者年觀察數據，已全面驗證 Alirocumab 在急性冠心症後患者中的心血管事件降低效益與長期安全性（PMID: 38658193）。多篇 2024–2025 年高質量文獻亦持續更新 PCSK9 抑制劑在膽固醇代謝障礙系列疾病中的療效與機轉研究，為香港市場引進提供充分的科學依據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03207945](https://clinicaltrials.gov/study/NCT03207945) | Phase 3 | 完成 | 118 | EPIC-HIV 研究：PCSK9 抑制劑用於 HIV 感染合併高脂血症患者，評估血管發炎、內皮功能及非鈣化斑塊等心血管風險指標。**注意**：本試驗實際使用藥物為 Evolocumab（非 Alirocumab），屬同類效應（class effect）映射，Alirocumab 直接適用性需另行確認。 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39947256](https://pubmed.ncbi.nlm.nih.gov/39947256/) | 2025 | Review | Pharmacology & Therapeutics | Alirocumab 與 Evolocumab 作用於細胞外 PCSK9，與 inclisiran（siRNA 抑制肝內 PCSK9 合成）的機轉比較、療效差異及臨床選用考量 |
| [38185721](https://pubmed.ncbi.nlm.nih.gov/38185721/) | 2024 | Review | Signal Transduction and Targeted Therapy | PCSK9 在脂質代謝、CVD、肝病、感染症、自免疾患及癌症中的廣泛角色，從基礎到臨床的全面回顧 |
| [38277255](https://pubmed.ncbi.nlm.nih.gov/38277255/) | 2024 | Review | Current Opinion in Lipidology | PCSK9 靶向療法更新：兩大 CVD 終點試驗回顧及 siRNA、疫苗等新型抑制策略展望 |
| [39751968](https://pubmed.ncbi.nlm.nih.gov/39751968/) | 2025 | Review | Current Atherosclerosis Reports | 同合子型家族性高膽固醇血症（HoFH）新型藥物治療進展，含 Alirocumab 的療效討論及局限性 |
| [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/) | 2024 | 安全性分析 | European Heart Journal. CVP | ODYSSEY OUTCOMES：47,296 患者年觀察，Alirocumab 安全性深度分析；復發性缺血事件及全因死亡率顯著降低，整體不良事件與安慰劑組相當 |
| [39679827](https://pubmed.ncbi.nlm.nih.gov/39679827/) | 2025 | Review | Pharmacotherapy | PCSK9 靶向療法現況與展望：他汀類降脂不足情境下，Alirocumab 的治療定位與 LDL-C 達標策略 |
| [37686091](https://pubmed.ncbi.nlm.nih.gov/37686091/) | 2023 | Review | Int J Molecular Sciences | 血脂異常治療進展：TC、TG、LDL-C 控制策略與整體心血管預後改善的全面分析 |
| [36739653](https://pubmed.ncbi.nlm.nih.gov/36739653/) | 2023 | Review | Kardiologia Polska | PCSK9 抑制劑降低心血管事件的臨床證據光譜：生化研究、基因體學及大型試驗結果整合回顧 |
| [36411665](https://pubmed.ncbi.nlm.nih.gov/36411665/) | 2022 | Review | Biomedicine & Pharmacotherapy | PCSK9 抑制劑安全性：歐洲 43% 他汀使用者未達 LDL-C 目標，PCSK9 抑制劑的安全性評估與補充治療角色 |
| [34070931](https://pubmed.ncbi.nlm.nih.gov/34070931/) | 2021 | Review | Int J Molecular Sciences | PCSK9 生物學及其在動脈粥狀硬化血栓形成（atherothrombosis）中的核心調控角色 |

---

## 香港上市資訊

Alirocumab 目前在香港**尚未取得上市許可**，香港衛生署藥劑業及毒藥管理局（Pharmacy and Poisons Board）無任何已登記許可證。如需在香港使用，需另行申請藥品註冊或進口許可。

---

## 安全性考量

安全性資訊請參考原廠仿單。

根據 ODYSSEY OUTCOMES 試驗（PMID: [38658193](https://pubmed.ncbi.nlm.nih.gov/38658193/)）的 47,296 患者年觀察數據，Alirocumab 整體安全性良好，最常見不良反應為注射部位反應及鼻咽炎，嚴重不良事件發生率與安慰劑組無顯著差異。完整警語、禁忌及藥物交互作用資訊，請查閱 Sanofi/Regeneron 原廠仿單（Praluent® prescribing information）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Alirocumab 在膽固醇代謝障礙領域具備極強的機轉合理性——其核心機轉（PCSK9 抑制 → LDL 受體上調 → LDL-C 清除增加）與目標疾病病理直接對應；ODYSSEY OUTCOMES 等多項大型試驗已充分建立全球療效與安全性數據基礎。惟香港目前尚無上市許可，且本地仿單警語與作用機轉資料存在資料缺口，需於推進前補全。

**若要推進需要：**

- **監管申請**：向香港衛生署藥劑業及毒藥管理局申請 Alirocumab 藥品註冊，或評估個案進口許可途徑
- **補充安全性資料（DG001）**：取得並解析 Praluent® 原廠仿單，確認詳細警語、禁忌症及藥物交互作用
- **補充作用機轉資料（DG002）**：查詢 DrugBank API（DB09302）取得完整 pharmacology 及 targets 資訊
- **類效應確認**：評估 EPIC-HIV 試驗（NCT03207945，Evolocumab）數據對 Alirocumab 的同類效應外推適用性，必要時尋找 Alirocumab 直接試驗數據
- **延伸研究問題**：評估黃色瘤病（xanthomatosis，Rank 3，L4）作為下一階段研究方向的可行性，現有 2 篇案例報告（PMID: 31538826、32713907）提供間接支持，建議設計前瞻性病例系列研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

