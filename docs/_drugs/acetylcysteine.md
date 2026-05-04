---
layout: default
title: Acetylcysteine
parent: 高證據等級 (L1-L2)
nav_order: 19
evidence_level: L1
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine：從黏液溶解到血栓性疾病

## 一句話總結

Acetylcysteine（NAC）是廣為人知的黏液溶解劑，在全球被核准用於呼吸道疾病及乙醯胺酚中毒解毒，惟香港目前未取得上市許可。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic Disease)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多個已完成的 Phase 2/3 隨機對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黏液溶解劑 / 乙醯胺酚中毒解毒（全球已知用途；香港未取得上市許可） |
| 預測新適應症 | 血栓性疾病 (Thrombotic Disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

NAC 的核心化學特性在於其游離巰基（-SH），可直接還原並裂解超大型 VWF（ULVWF）多聚體的二硫鍵。ULVWF 多聚體因 ADAMTS13 酵素缺乏而異常堆積，是血栓性血小板減少性紫癜（TTP）及移植相關血栓性微血管病（TA-TMA）的核心病理機轉。NAC 透過物理化學手段截斷此鏈，降低血小板異常聚集，與其他機轉互補而非重疊。

此外，NAC 作為麩胱甘肽（GSH）的前驅物，可系統性提升細胞內抗氧化能力，抑制活性氧（ROS）誘發的內皮損傷及凝血級聯過度活化。在糖尿病腦中風模型中，NAC 已被證實可逆轉甲基乙二醛（MG）糖化蛋白所造成的系統性血小板過度活化（PMID 28961512）；在腎功能不全患者中，RENACTIF 雙盲 RCT（NCT03636932）直接顯示 NAC 可降低尿毒素（Indoxyl Sulfate）誘發的血栓表型。

上述雙重機轉（VWF 多聚體還原 ＋ GSH 抗氧化）已在 baboon 及 mouse 的 TTP 動物模型獲得直接驗證（PMID 28011677），並延伸至多個人體臨床試驗，使 TxGNN 的預測具有完整的機轉鏈支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | 已完成 | 170 | HSCT 相關 TA-TMA 患者中，NAC 靜脈給藥的前瞻性安全性與療效評估，為本適應症迄今最高等級直接證據 |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | 未知（需確認） | 260 | 評估異體造血幹細胞移植後 NAC 預防血栓事件的療效與安全性，規模最大的直接預防性研究 |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | 進行中（停止招募） | 44 | 多中心前瞻性單臂試驗，評估 NAC 治療 TA-TMA 的療效，補充驗證 NCT03252925 的結果 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | 已完成 | 40 | RENACTIF 雙盲隨機交叉試驗，慢性腎病患者中 NAC 顯著降低 Indoxyl Sulfate 誘發的血栓表型，直接切合氧化-凝血機轉 |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | 未知 | 44 | 新診斷 ITP 患者中 NAC 聯合高劑量地塞米松的開放標籤單臂試驗，與血栓-止血軸間接相關 |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | 未知 | 200 | 阿托伐他汀＋NAC＋達那唑三聯療法用於類固醇抵抗性 ITP，NAC 為組合用藥之一 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | 已完成 | 15 | 探索性試驗評估 NAC＋阿托伐他汀對類固醇抵抗性 ITP 血小板計數的影響，規模小 |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | 已完成 | 3 | 疑似 TTP 患者中 NAC 靜脈給藥先導研究，驗證 NAC 促進 ADAMTS13 裂解 VWF 的概念 |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | 尚未招募 | 30 | 重型再生不良性貧血患者半相合移植後，NAC 促進造血恢復的單臂研究，目標族群偏離血栓主軸 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | 回顧性世代研究 | Annals of Hematology | NAC 治療與獲得性 TTP 院內死亡率之關聯性分析，肯定 NAC 在 aTTP 治療中的地位 |
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplantation and Cellular Therapy | 前瞻性隨機安慰劑對照試驗，NAC 預防 TA-TMA 的療效評估，提供高質量人體預防性證據 |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | 機轉研究 | Journal of Clinical Investigation | NAC 可在人類血漿及小鼠體內直接縮小並降低 VWF 多聚體活性，奠定最核心的分子機轉基礎 |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | 前臨床（小鼠/狒狒） | Blood | NAC 在 TTP 的 baboon 及 mouse 動物模型中改善血小板計數及出血時間，為最完整的動物模型驗證 |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review（含再利用藥物策略） | Expert Review of Hematology | 系統性回顧 TTP 再利用藥物（含 NAC、rituximab、caplacizumab），肯定 NAC 的再利用潛力 |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP 病理生理、診斷與治療完整回顧，ADAMTS13-VWF 軸為核心靶點 |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | TTP 機轉權威性回顧，強調 ADAMTS13 缺乏與 VWF 多聚體在微血管血栓中的關鍵作用 |
| [28382967](https://pubmed.ncbi.nlm.nih.gov/28382967/) | 2017 | Review | Nature Reviews Disease Primers | TTP 疾病全面概述，含發病機轉、診斷、治療及預後，為領域標竿文獻 |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Review（管理指引） | Transfusion Clinique et Biologique | TTP 管理策略回顧，TPE 為主軸，NAC 作為輔助/難治性治療選項被提及 |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review（COVID/血栓） | Journal of Infection and Public Health | NAC 用於 COVID-19 之評估，涵蓋其對抗血栓前狀態（prothrombotic state）的機轉分析 |

---

## 香港上市資訊

Acetylcysteine 目前在香港**未取得上市許可**，無任何已批准的藥品許可證（HK License）紀錄。若需在香港使用，須另行申請特殊用藥途徑（如未經註冊藥物申請）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：本次 Evidence Pack 未能取得香港仿單警語、禁忌症及藥物交互作用資料（資料缺口 DG001）。如需進行安全性評估，建議優先查閱 EMA 或 FDA 核准的 Acetylcysteine 說明書，以及 DrugBank DB06151 的安全性條目。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 2 個已完成的 Phase 2/3 臨床試驗（NCT03252925, NCT03636932）及 1 個正進行中的 Phase 2/3 試驗（NCT07279610）直接支持 NAC 用於血栓性微血管病，加上 2011 年 *Journal of Clinical Investigation* 的核心機轉研究（PMID 21266777）確立了 NAC 降解 ULVWF 多聚體的分子基礎，證據鏈完整，達到 L1 等級。NAC 作為 FDA 核准的既有藥物，安全性資料積累豐富，再利用風險相對可控。

**若要推進需要：**
- 取得 NAC 作用機轉（MOA）完整資料（建議查詢 DrugBank DB06151 API，修補 DG002）
- 取得香港仿單警語與禁忌症（修補 DG001），完成 S1 安全性初評
- 確認 NCT05907486 的最新試驗狀態（目前標示 UNKNOWN）
- 評估香港使用 NAC 的法規路徑（未上市藥品特殊申請流程）
- 若針對 TA-TMA 適應症推進，建議參照 NCT03252925 試驗設計，規劃本地患者的回顧性病歷分析作為先行可行性評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

