---
layout: default
title: Axitinib
parent: 僅模型預測 (L5)
nav_order: 76
evidence_level: L5
indication_count: 10
---

# Axitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Axitinib：從晚期腎細胞癌到 Xp11.2 易位/TFE3 融合型腎細胞癌

## 一句話總結

Axitinib（Inlyta®）是第二代口服高選擇性 VEGFR-1/2/3 酪胺酸激酶抑制劑，國際上已廣泛核准用於晚期腎細胞癌（RCC）治療，但目前在香港尚無上市許可。TxGNN 模型預測它對 **Xp11.2 易位/TFE3 基因融合型腎細胞癌（tRCC）** 具有療效潛力，此為一種主要影響青少年與年輕成人、預後不佳且缺乏標準治療的罕見 RCC 亞型。目前有 **1 個 Phase 2 臨床試驗**（進行中）和 **2 篇病例報告**直接針對此亞型，加上廣義 RCC 領域數十個高品質臨床試驗（含多個 Phase 3 RCT）作為機轉旁證，整體科學基礎紮實。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 晚期腎細胞癌（國際已核准；香港目前無上市許可） |
| 預測新適應症 | Xp11.2 易位/TFE3 基因融合型腎細胞癌 (tRCC) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L3（tRCC 直接證據）；廣義 RCC 達 L1 |
| 香港上市 | ✗ 未上市（0 張許可證） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Axitinib 是目前同類藥物中對 VEGFR 親和力最強的口服 TKI，其對 VEGFR-1、VEGFR-2、VEGFR-3 的 IC50 達皮莫爾（pM）級，比 sunitinib、sorafenib 等第一代 VEGFR 抑制劑強約 10 倍。核心作用機轉是阻斷 VEGF 介導的腫瘤血管新生訊號通路，在透明細胞 RCC 中則具體切斷 VHL 突變 → HIF-1α 累積 → VEGF 過度分泌 → 腫瘤血管生成的致癌鏈路。

Xp11.2 易位/TFE3 融合型 RCC 的致病機轉與 Axitinib 的作用靶點高度契合。TFE3 轉錄因子在染色體易位後與多種夥伴基因（PRCC、ASPSCR1、SFPQ 等）形成異常融合蛋白，異常活化下游靶基因，包括直接上調 VEGF-A 的轉錄表達，導致腫瘤微環境 VEGF 訊號持續過度活化及豐富的病理性血管新生。此路徑雖與透明細胞 RCC 的 VHL-HIF 軸有所不同，但最終均匯聚至 VEGFR 下游效應，使 Axitinib 的抗血管新生機轉具有直接的理論依據。

臨床觀察進一步支持此連結：文獻報告顯示 tRCC 患者對 VEGFR-TKI 單藥治療有部分（但非持久）的腫瘤反應，提示此亞型並非對 TKI 天然抵抗。聯合免疫檢查點抑制劑（如 nivolumab）的策略，可同時針對血管新生與 PD-1 介導的免疫逃脫，兼具協同抗腫瘤潛力，正是 NCT03595124 隨機對照試驗的設計核心。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Phase 2 | 進行中（不再招募） | 15 | 隨機試驗直接比較 Axitinib＋Nivolumab 組合療法 vs. 單藥 Nivolumab，針對不可切除或轉移性 TFE/易位型 RCC（含 Xp11.2/TFE3 亞型），涵蓋所有年齡層（兒童至成人）。試驗尚未公布療效結果，但招募完成代表臨床可行性已確立，設計合理性獲研究者支持；預計 2026 年 11 月完成。 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36034832](https://pubmed.ncbi.nlm.nih.gov/36034832/) | 2022 | Case Report | Frontiers in Pharmacology | 32 歲男性成人 Xp11.2 tRCC 伴淋巴結及器官轉移，以 camrelizumab（PD-1 抑制劑）聯合 axitinib 治療後達到臨床完全緩解（cCR），為此罕見亞型採用 IO＋VEGFR-TKI 組合策略成功的首批病例報告之一。 |
| [36246795](https://pubmed.ncbi.nlm.nih.gov/36246795/) | 2022 | Case Report | World Journal of Clinical Cases | T3aN1M1 期巨大 Xp11.2/TFE3 tRCC 患者，接受化療、動脈化學栓塞及腎切除術的多模式治療，詳細記錄此亞型的臨床特性與治療挑戰，作為標準治療侷限性的背景對照，間接支持新型靶向策略的探索必要性。 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（VEGFR-TKI 類）；非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 低（VEGFR-TKI 類骨髓毒性顯著低於傳統化療；中性粒細胞減少非主要不良反應） |
| 致吐性分級 | 低 |
| 監測項目 | 血壓（高血壓為最常見不良反應，發生率達 40%）、甲狀腺功能（甲狀腺功能低下）、CBC（含分類）、肝腎功能、尿蛋白 |
| 處置防護 | 需依細胞毒性藥物處置規範操作；口服劑型應完整吞服，不可磨碎或切割 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Axitinib 對 Xp11.2 tRCC 的機轉連結清晰合理（TFE3 融合 → VEGF 過度活化 → VEGFR 可干預），已有 Phase 2 隨機對照試驗（NCT03595124）正在直接驗證此假說，且廣義 RCC 領域存在多個已完成的 Phase 3 RCT（KEYNOTE-426、JAVELIN Renal 101、RENOTORCH），提供了強有力的藥物安全性與療效旁證（L1 級）。此罕見亞型目前缺乏標準治療，IO＋TKI 組合策略具臨床合理性，值得積極追蹤進展。

**若要推進需要：**
- 持續追蹤 NCT03595124 結果（預計 2026 年 11 月完成），此為目前最關鍵的直接證據來源
- 補充 Axitinib 在香港的上市許可狀態及仿單安全警語（DG001 資料缺口）
- 評估此稀有亞型的分子篩檢（TFE3 FISH 或 RNA 融合檢測）作為患者選擇依據
- 兒童及青少年族群若為治療對象，需另行評估兒童藥動學數據（參考 PMID 39326645 綜述）
- 建議設計規範性收案框架（如 registry study），累積香港地區 tRCC 患者的真實世界數據

---

> ⚠️ **免責聲明**：本報告僅供研究參考，不構成醫療建議。藥物再利用候選需經嚴格臨床驗證方可應用於患者治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

