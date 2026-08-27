---
layout: default
title: Probenecid
parent: 中證據等級 (L3-L4)
nav_order: 416
evidence_level: L4
indication_count: 3
---

# Probenecid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Probenecid：從痛風／高尿酸血症到腎性低尿酸血症

## 一句話總結

Probenecid 是一款尿酸排泄劑（uricosuric agent），傳統上用於痛風與高尿酸血症的治療。TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, Renal)** 有效，目前有 **0 個臨床試驗**和 **20 篇文獻**與此方向相關，但需特別留意：這批文獻大多將 probenecid 作為「診斷測試試劑」而非治療藥物使用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、高尿酸血症（尿酸排泄劑；香港未上市，無許可證資料可佐證原核准適應症） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經 DrugBank API 查證的詳細作用機轉資料（MOA 標記為資料缺口 DG002）。根據一般藥理學知識，Probenecid 屬於尿酸排泄劑，透過抑制腎近端小管的有機陰離子轉運蛋白（如 OAT1/OAT3），阻斷尿酸等有機陰離子的再吸收，促使尿酸經尿液排出，臨床上用於治療痛風與高尿酸血症，過去也曾用於延緩青黴素類抗生素的腎臟排除。

**這裡有一個需要特別提出的矛盾點**：腎性低尿酸血症患者的病理生理是尿酸「經腎臟排泄過多」（多因 URAT1/SLC22A12 轉運蛋白突變導致尿酸重吸收缺陷），而非排泄不足。Probenecid 的藥理作用方向恰好相反——它會進一步抑制尿酸重吸收、促進尿酸排泄，理論上可能加重而非改善此病的尿酸流失，甚至增加運動誘發急性腎衰竭的風險（多篇附錄文獻中提及此併發症）。

檢視這 20 篇文獻可發現，多數研究並非把 probenecid 當作治療藥物來評估，而是利用「probenecid 試驗」（常與 pyrazinamide 試驗並用）作為**診斷工具**，用來鑑別患者近端小管尿酸轉運缺陷的亞型（presecretory reabsorption 缺陷、postsecretory reabsorption 缺陷、或分泌增加型）。換言之，TxGNN 模型很可能是從「probenecid 與 renal hypouricemia 在文獻中高度共現」這個統計關聯學習到此預測，而不是反映真正具治療潛力的機轉關係。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical rheumatology | 低尿酸血症總論回顧，涵蓋腎性低尿酸血症病因與臨床意義 |
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Review | Molecular genetics and metabolism | 遺傳性腎性低尿酸血症之分子機轉回顧（SLC22A12/URAT1 突變） |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | 臨床/分子分析 | Journal of the American Society of Nephrology | 32 例日本特發性腎性低尿酸血症患者之 SLC22A12 基因定序與臨床相關性分析 |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | 病例報告＋文獻回顧 | American journal of kidney diseases | 腎性低尿酸血症併運動誘發急性腎衰竭之預防與文獻回顧 |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | 病例報告 | Nephron | 新型腎性低尿酸血症：對 pyrazinamide 與 probenecid 均無反應之混合型缺陷 |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | 病例報告 | Nephron | 腎性低尿酸血症合併尿路結石，以 probenecid/benzbromarone 測試分泌增加型缺陷，並以尿液鹼化成功治療結石 |
| [7933674](https://pubmed.ncbi.nlm.nih.gov/7933674/) | 1994 | 病例報告 | Nihon Jinzo Gakkai shi | 不完全混合型腎性低尿酸血症，probenecid 僅使尿酸排泄輕微增加 |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | 病例報告 | Nephron | 家族性低尿酸血症，對 probenecid 與 pyrazinamide 反應皆減弱，顯示近端腎小管重吸收缺陷 |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | 病例報告 | Nephron | 家族性腎性低尿酸血症併特發性水腫，probenecid 反而使尿酸排泄矛盾性下降 |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | 病例報告 | Archives of internal medicine | 糖尿病性腎性低尿酸血症，以 pyrazinamide 可抑制之尿酸清除率增加作為機轉證據 |

---

## 香港上市資訊

Probenecid 目前於香港**未上市**，查無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本評估的關鍵安全性資料（仿單警語、禁忌症）在 Evidence Pack 中被標記為 **Blocking 等級資料缺口（DG001）**，代表目前無法完成 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一具備一定文獻量的預測方向（腎性低尿酸血症）在藥理邏輯上與 Probenecid 的尿酸排泄作用方向相反，且 20 篇支持文獻多屬診斷性/機轉性質（probenecid 試驗），並非治療性研究，也無任何臨床試驗佐證（0 篇）。
- 關鍵安全性資料（仿單警語與禁忌）缺失，且列為 Blocking 等級資料缺口（DG001），無法完成 S1 安全性初評。
- 藥物於香港未上市（0 張許可證），推進前需另行確認在地取得管道與法規路徑。
- 同一藥物在 TxGNN 排序中的其他兩個高分預測（Lesch-Nyhan 症候群、HGPRT 部分缺乏）皆屬尿酸「過量生成」疾病，其中 Lesch-Nyhan 方向已有文獻明確提示 probenecid 使用可能提高尿酸性腎病變風險。三個方向合併來看，顯示模型很可能是被「probenecid＋尿酸代謝」的文獻共現關係帶動，而非穩固一致的治療性訊號。

**若要推進需要：**
- 補齊 DrugBank／原廠仿單完整 MOA 與安全性資料（對應 DG002、DG001 之補救措施）
- 釐清 probenecid 在腎性低尿酸血症文獻中是否僅具診斷用途，或確有機轉支持其可能的治療角色
- 針對 Lesch-Nyhan 症候群、HGPRT 部分缺乏兩個方向做尿酸「生成 vs. 排泄」機轉的交叉驗證，避免同一藥物在矛盾方向上被誤判為有效
- 補充香港上市登記與取得管道資訊（目前 0 張許可證、未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

