---
layout: default
title: Chlordiazepoxide
parent: 中證據等級 (L3-L4)
nav_order: 161
evidence_level: L4
indication_count: 10
---

# Chlordiazepoxide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Chlordiazepoxide：從焦慮症到失眠

## 一句話總結

Chlordiazepoxide（氯二氮平，商品名 Librium）是苯二氮平類（Benzodiazepine）的始祖藥物，自 1961 年起以焦慮症及酒精戒斷治療聞名，其 GABA-A 受體調節機轉在理論上同樣適用於助眠。TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，預測分數高達 **99.998%**。目前有 **6 篇相關文獻**支持此方向，但缺乏直接相關的臨床試驗，且其極長半衰期帶來的次晨宿醉效應，是現代失眠治療的主要限制因素。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 焦慮症（依文獻推斷；原始資料欄位為空） |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 待補充）。根據已知資訊，Chlordiazepoxide 是苯二氮平類的首個成員（1955 年由 Leo Sternbach 於羅氏藥廠合成），在焦慮症治療中的療效已由數十年臨床使用所確立。其作用機轉透過與 GABA-A 受體的苯二氮平位點結合，正向調節（PAM）γ-胺基丁酸介導的抑制性突觸傳遞，產生廣泛中樞神經系統抑制效果，機轉上可能適用於失眠。

焦慮症與失眠高度共病，GABA-A 受體調節是兩者共同的藥理靶點。苯二氮平類藥物的助眠機轉體現在縮短睡眠潛伏期、增加總睡眠時間、減少夜間覺醒，並可能抑制 REM 睡眠。TxGNN Rank 6 亦同步預測其對「睡眠起始與維持障礙 (Sleep Disorder, Initiating and Maintaining Sleep)」有效（預測分數 99.877%），兩個預測方向高度一致，進一步支持此推斷。

然而，Chlordiazepoxide 的消除半衰期長達 24–48 小時，且活性代謝物去甲氯二氮平（desmethylchlordiazepoxide）半衰期更長，導致次晨宿醉效應（殘餘鎮靜、精神運動損害、認知模糊）顯著，尤其在老年族群中風險倍增。現代失眠治療指引已轉向短中效 BZD（如 temazepam、triazolam）或非苯二氮平類 Z 藥（如 zolpidem、eszopiclone），Chlordiazepoxide 的臨床地位已大幅式微。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

> **資料管道注意**：資料庫映射到一個試驗 [NCT01109030](https://clinicaltrials.gov/study/NCT01109030)（吡格列酮輔助 Citalopram 用於中重度抑鬱症，Phase 2/3，N=50，已完成），但該試驗與 Chlordiazepoxide 或失眠均無直接關聯，屬嚴重資料錯配（相關性評級：C，資料管道映射錯誤），已排除。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [3536890](https://pubmed.ncbi.nlm.nih.gov/3536890/) | 1986 | RCT | J Clin Psychiatry | Limbitrol（氯二氮平＋阿米替林複方）vs 阿米替林：Limbitrol 組失眠與焦慮症狀改善速度更快；兩組睡眠結構各期（Stage 1–4）改善幅度無顯著差異 |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | 系統性回顧 | J Fam Pract | 苯二氮平類用於社區老年失眠患者：10 個符合標準研究顯示短期有效（縮短入睡時間、增加睡眠時間）；跌倒、認知損害風險值得關注；長期療效資料缺乏 |
| [22521806](https://pubmed.ncbi.nlm.nih.gov/22521806/) | 2013 | 批判性回顧 | Eur Psychiatry | Chlordiazepoxide 作為第一個 BZD 已使用逾 50 年；BZD 在精神科治療仍具地位，但依賴形成、認知副作用及停藥困難為核心問題，需謹慎評估長期使用 |
| [2883822](https://pubmed.ncbi.nlm.nih.gov/2883822/) | 1986 | 臨床回顧 | Acta Psychiatr Scand Suppl | 老年人對苯二氮平類藥動學反應較年輕人增加 2–3 倍，非僅因血漿濃度改變，年齡相關藥效動力學敏感性升高需審慎調整劑量 |
| [30680986](https://pubmed.ncbi.nlm.nih.gov/30680986/) | 2019 | 橫斷面研究 | Med Glasnik | 伊朗老年患者潛在不適當用藥（PIM）調查（Beers 2012 標準）：苯二氮平類（含 Chlordiazepoxide）被列為老年人 PIM，與健康照護資源使用增加相關 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | 敘述性回顧 | Expert Opin Drug Metab Toxicol | 焦慮藥物（含苯二氮平類）藥動學綜述：BZD 為西方最常處方精神科藥物，藥動學差異顯著影響臨床效果與殘餘鎮靜風險，強調個體化用藥 |

> **說明**：PMID 3536890 及 7595266 引自 TxGNN Rank 6「睡眠起始與維持障礙」之文獻庫，與失眠主題高度相關，納入最相關文獻清單；其中 PMID 3536890 為直接包含 Chlordiazepoxide 的睡眠 RCT，具最高直接證據價值。

---

## 香港上市資訊

Chlordiazepoxide 目前在香港**無上市許可證登記（0 張）**，屬未上市狀態，任何臨床應用均需從頭啟動本地上市流程。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Chlordiazepoxide 透過 GABA-A 正向調節機轉在理論上具助眠潛力，TxGNN 預測分數亦高，但目前缺乏直接針對本藥的高品質失眠試驗，且其極長半衰期（24–48 h）帶來顯著的次晨宿醉與認知損害風險；加上 MOA 資料與安全性資料均缺失，香港亦尚未上市，現階段不建議推進。

**若要推進需要：**
- 補充完整 MOA 資料（DrugBank API 查詢 DB00475）
- 取得安全性資料：仿單警語、禁忌症及藥物交互作用資料庫
- 設計直接比較 Chlordiazepoxide 與短效 BZD（如 temazepam）或 Z 藥的隨機對照失眠試驗
- 完整評估老年族群及呼吸功能不全患者的風險效益比
- 若考慮香港市場，需啟動衛生署本地藥物登記申請
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

