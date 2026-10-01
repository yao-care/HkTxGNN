---
layout: default
title: Voxilaprevir
parent: 僅模型預測 (L5)
nav_order: 928
evidence_level: L5
indication_count: 5
---

# Voxilaprevir
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

# Voxilaprevir：從慢性 C 型肝炎到 B 型肝炎病毒感染

## 一句話總結

Voxilaprevir 是 Vosevi（sofosbuvir/velpatasvir/voxilaprevir）複方的成分之一，用於治療 C 型肝炎。
TxGNN 模型預測它可能對 **B 型肝炎病毒感染 (Hepatitis B virus infection)** 有效。
但目前 5 個臨床試驗和 9 篇文獻**全部針對 C 型肝炎**，沒有直接的 B 型肝炎療效證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎（許可證未載明適應症，依臨床試驗與機轉資料判斷） |
| 預測新適應症 | B 型肝炎病毒感染 (Hepatitis B virus infection) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5（僅有模型預測，無 B 型肝炎的直接研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知資訊，Voxilaprevir 是 HCV NS3/4A 絲胺酸蛋白酶抑制劑，在 Vosevi 複方中與 sofosbuvir、velpatasvir 併用，其在 C 型肝炎的療效已被證實。

不過，機轉上並不支持用於 B 型肝炎。HBV 沒有同源的蛋白酶，複製依賴反轉錄聚合酶，而 Voxilaprevir 並不作用於這個標的。

0.998 的高分較可能反映知識圖譜中「肝炎／抗病毒」節點的鄰近性，而不是共同的藥物標的。

與 B 型肝炎唯一有臨床關聯的是**安全性訊號**：C 型肝炎直接抗病毒藥物（DAA）治療，對 HBV/HCV 共同感染者有 HBV 再活化的類別警語。

## 臨床試驗證據

以下 5 個試驗皆為 C 型肝炎研究，**不能視為 B 型肝炎療效證據**。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03823911](https://clinicaltrials.gov/study/NCT03823911) | Phase 4 | 完成 | 87 | HIV/HCV 患者 HCV 根除後的心血管風險；與 HBV 無關 |
| [NCT04695769](https://clinicaltrials.gov/study/NCT04695769) | Phase 4 | 完成 | 281 | Ribavirin 併用 SOF/VEL/VOX 於慢性 C 型肝炎治療失敗者的隨機試驗；無 HBV 療效指標 |
| [NCT06180590](https://clinicaltrials.gov/study/NCT06180590) | N/A | 招募中 | 200 | Vosevi 用於 DAA 治療失敗的 HCV 患者之前瞻性世代研究；無 HBV 療效指標 |
| [NCT02938013](https://clinicaltrials.gov/study/NCT02938013) | Phase 4 | 完成 | 15 | 比較兩種與三種 DAA 對 HCV 動力學與肝臟的影響；未涉及 HBV |
| [NCT02533427](https://clinicaltrials.gov/study/NCT02533427) | Phase 1 | 完成 | 15 | 與荷爾蒙避孕藥的藥物交互作用（PK）研究；與 HBV 無關 |

## 文獻證據

以下文獻皆以 HCV 或病毒性肝炎為主題，無 B 型肝炎療效研究。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35248212](https://pubmed.ncbi.nlm.nih.gov/35248212/) | 2022 | 單臂試驗（世代） | Lancet Gastroenterol Hepatol | 盧安達 SHARED-3：SOF/VEL/VOX 用於 DAA 治療失敗的 HCV 再治療 |
| [36535062](https://pubmed.ncbi.nlm.nih.gov/36535062/) | 2022 | 世代研究 | J Gastrointestin Liver Dis | 羅馬尼亞真實世界資料：SOF/VEL/VOX 用於基因型 1b、DAA 無反應者 |
| [40611935](https://pubmed.ncbi.nlm.nih.gov/40611935/) | 2025 | 世代研究 | J Clin Exp Hepatol | 印度 HCV 消除計畫中抗藥性突變與 DAA 治療失敗預測因子 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA 治療失敗的 HCV 患者再治療 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | C 型肝炎治療的藥動學與藥效學考量（2019 更新） |
| [31915372](https://pubmed.ncbi.nlm.nih.gov/31915372/) | 2020 | Review | Nat Rev Gastroenterol Hepatol | 帶病毒器官移植與抗病毒治療的新進展 |
| [29369303](https://pubmed.ncbi.nlm.nih.gov/29369303/) | 2018 | 會議報告 | AIDS Rev | 2017 國際病毒性肝炎會議報告 |
| [30964552](https://pubmed.ncbi.nlm.nih.gov/30964552/) | 2019 | 體外／病毒學 | Hepatology | HCV 蛋白酶抑制劑逃逸變異株的演化路徑 |
| [40414600](https://pubmed.ncbi.nlm.nih.gov/40414600/) | 2025 | 價格分析 | Ann Hepatol | B 型與 C 型肝炎藥物的全球價格比較 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65775 | VOSEVI TABLETS（廠商：GILEAD SCIENCES HONG KONG LIMITED） | — | — |

## 安全性考量

- **主要警語**：DAA 治療 C 型肝炎，對 HBV/HCV 共同感染者有 HBV 再活化的類別警語（依機轉分析資料）。

其餘安全性資訊（禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有臨床試驗與文獻都針對 C 型肝炎。Voxilaprevir 的標的（NCT/NS3/4A 蛋白酶）在 HBV 中不存在，高預測分數很可能是知識圖譜的鄰近性假象。
- 同一批預測的其他項目也都是 Hold：
  - E 型肝炎、A 型肝炎：目標病毒蛋白酶與 HCV 不同，且 A 型肝炎相關的 31 個試驗全是 HCV 研究。
  - 「動物病毒性肝炎」：屬非人類的泛用本體節點，應為知識圖譜假象。
  - 鄂木斯克出血熱：僅有黃病毒科層級的推測性關聯。

**若要推進需要：**
- 補上香港衛生署仿單的警語與禁忌症（目前為阻擋性缺口，無法進入安全性篩選）
- 補上 DrugBank 的作用機轉資料
- 若仍想探索 HBV，需先做體外抗 HBV 活性試驗，確認有無標的外效應
- 在 HBV/HCV 共同感染者中，建立 HBV 再活化的監測流程（HBsAg、HBV DNA）

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

